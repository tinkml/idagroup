import os


def check_url(url: str) -> None:
    """Проверка пути в случае если пути к директории нет создает его."""
    if not os.path.exists(url):
        os.makedirs(url)


def reformat_file_name(file_name: str) -> str:
    new_file_name = file_name.strip().replace(' ', '_').split('.')[0]
    return new_file_name