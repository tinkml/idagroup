from enum import Enum
from typing import Optional


class FileFormats(Enum):

    # изображения
    jpg = 'jpg'
    jpeg = 'jpeg'
    png = 'png'

    @classmethod
    def get_file_format_by_filename(cls, file_name: str) -> Optional['FileFormats']:
        """Получаем формат файла (Enum) по полученному имени."""
        if file_name.endswith('.jpg'):
            return FileFormats.jpg
        elif file_name.endswith('.jpeg'):
            return FileFormats.jpeg
        elif file_name.endswith('.png'):
            return FileFormats.png
        else:
            return None
