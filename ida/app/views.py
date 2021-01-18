from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .enums import FileFormats
from .forms import UploadFileForm, EditImageForm
from .logic import upload_file_to_os, download_file, resize_image
from .utils import reformat_file_name
from .service import ServiceImage, ServiceResizedImage
from .settings import ADDRESS


def images_list(request):
    """Получаем список всех изображений."""
    images = ServiceImage.get_all_images()
    resized_images = ServiceResizedImage.get_all_images()
    return render(request, 'app/home.html', {'images': images, 'resized_images': resized_images})


def upload_image(request) -> HttpResponse:
    """Загрузка изображения в ОС"""

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)  # Создаем форму с данными из запроса, для дальнейшей валид.

        if form.is_valid():  # В случае, если данные валидны.
            file = request.FILES.get('file', None)  # Пытаемся получить файл.

            data = dict()  # Словарь, с данными для записи в БД
            if not file:  # В случаем, если файла нету.
                link_to_download_file = request.POST.get('url', None)  # Пытаемся получить ссылку для скачивания
                if not link_to_download_file:  # Если ссылки нет, делаем редирект на страницу с ошибкой.
                    return render(request, 'app/error.html', {'error': 'No links or file to upload'})

                file = download_file(url=link_to_download_file)  # Загружаем файл в ОС
                data.update(url=link_to_download_file)  # Обновляем словарь с данными, если была получена ссылка
                return render(request, 'app/error.html', {'error': 'The functionality is still in development'})

            file_name = reformat_file_name(file_name=file.name)  # Форматируем назвние для использования в пути url
            file_format = FileFormats.get_file_format_by_filename(file_name=file.name).value
            data.update(name=file_name, file_format=file_format)

            full_file_name = f'{file_name}.{file_format}'
            upload_file_to_os(file, full_file_name)  # Сохраняем файл в ОС.

            ServiceImage.create(data=data)  # оздаем объект модели Image

            return HttpResponseRedirect(f'{ADDRESS}/resize/{file_name}/')  # Редиректим пользователя на стран-у редакт-я
    else:

        form = UploadFileForm()  # Создаем форму для загрузки изображения.
    return render(request, 'app/upload.html', {'form': form})  # Отдаем форму на фронт.


def edit_image(request, filename) -> HttpResponse:
    """Изменение размера изображения."""

    image = ServiceImage.get_by_name(name=filename)  # Проверяем, есть ли в БД запись о изображении, с таким названием
    if image is None:  # Если в БД нет записи об этом изображении, отдаем страницу с ошибкой
        return render(request, 'app/error.html', {'error': 'No image with that name'})

    full_file_name = f'{filename}.{image.file_format}'  # Получаем название файла, вместе с расширением.

    if request.method == 'POST':

        form = EditImageForm(request.POST)
        if form.is_valid():
            width = request.POST.get('width')
            height = request.POST.get('height')

            width = int(width) if width is not '' else None
            height = int(height) if height is not '' else None

            if not width and not height:  # Проверяем, если не указан ни один из параметров, отдаем страницу с ошибкой
                return render(request, 'app/error.html', {'error': 'No new parameters to resize image'})

            if width == 0 or height == 0:  # Проверяем, если указан 0 как параметр, отдаем страницу с ошибкой
                return render(request, 'app/error.html', {'error': 'Zero can not be the parameter to resize image'})

            resized_file_name = resize_image(file_name=full_file_name, new_width=width, new_height=height)

            data = dict(name=resized_file_name, original_image=image)  # Формируем словарь с данными, для записи в БД
            ServiceResizedImage.create(data=data)  # Создаем запись об измененном изображении

            return render(request, 'app/resize.html', {'form': form, 'image_url': f'/static/media/{resized_file_name}'})

    else:
        form = EditImageForm()
    return render(request, 'app/resize.html', {'form': form, 'image_url': f'/static/media/{full_file_name}'})


