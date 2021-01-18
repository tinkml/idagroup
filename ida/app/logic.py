from PIL import Image
from django.core.files import File

from .settings import FILE_PATH


def upload_file_to_os(file: File, filename: str) -> None:
    """Сохранение файла в ОС"""
    full_file_name = f'{FILE_PATH}/{filename}'
    with open(full_file_name, 'wb+') as new_file:
        for chunk in file.chunks():
            new_file.write(chunk)


def reformat_file_name(file_name: str) -> str:
    new_file_name = file_name.strip().replace(' ', '_').split('.')[0]
    return new_file_name


def download_file(url: str):
    return ''


def resize_image(file_name: str, new_width: int = None, new_height: int = None) -> str:
    """Изменение размера изображения."""

    full_file_name = f'{FILE_PATH}/{file_name}'
    resized_file_name = f'edit_{file_name}'
    resized_file_path = f'{FILE_PATH}/{resized_file_name}'

    img = Image.open(full_file_name)

    if new_width is None and new_height is None:
        raise ValueError('No new parameters to resize image')

    if new_width == 0 or new_height == 0:
        raise ValueError('Zero can not be the parameter to resize image')

    width, height = img.size
    aspect_ratio = width / height

    if new_width is None:
        new_width = round(new_height * aspect_ratio)

    elif new_height is None:
        new_height = round(new_width / aspect_ratio)

    resize = img.resize((new_width, new_height), Image.ANTIALIAS)
    resize.save(resized_file_path)

    return resized_file_name
