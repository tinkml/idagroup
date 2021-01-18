## Технологии:
- Django
- Pyenv
- Poetry

## Необходимо, чтобы были установленны:
- <a href="https://github.com/pyenv/pyenv">Pyenv</a>
- <a href="https://github.com/">GitHub</a>

## Чтобы начать использовать:
Склонируйте репозиторий с проектом:
```sh
git clone https://github.com/tinkml/idagroup.git
```

Перейдите в директорию проекта:
```sh
cd idagroup/ida
```

Установите в диреткории локальный python3.8.3:
```sh
pyenv local 3.8.3
```

Утановите с помощью pip менеджер зависимостей <a href="https://python-poetry.org/">Poetry</a>:
```sh
pip3 install poetry
```

Утановите зависимости и активируйте виртуальное окружение:
```sh
poetry install
poetry shell
```

Запустите проек django:
```sh
python manage.py runserver
```

Проект станет доступен по адресу 
```sh
http://127.0.0.1:8000
```

## Важно:
После активирования виртуального окружения с помощью Poetry,
убедитесь, что у вас указан корректный путь к интерпритатору python:
```sh
/корень/пользователь/.cache/pypoetry/virtualenvs/название_проекта/bin/python3.8
```
