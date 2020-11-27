# test-task_treesitenav
TreeSiteNav API

## Корневой URL:
/

## Репозиторий:
https://github.com/akornilkov/test-task_fileapi

## Авторы
 * Anton Kornilkov <anton-kornilkov@yandex.ru>

## Язык реализации
python 3.8.6

## Среда развертывания
Docker

## Описание сервиса(тех.задание)
Разработать REST API на базе django-rest-framework которое реализует CRUD операции с разделами сайта

## Документация
* TODO

## Описание реализации
* TODO

## Масштабируемость
Возможно масштабирование средствами `gunicorn`, путем добавления дополнительных worker-ов.

# Разработка

## Установка зависимостей

```bash
$ cd 
$ pyenv virtualenv 3.8.6 test-task_treesitenav // создание виртуального окружения для проекта
$ pyenv local test-task_treesitenav // установка виртуального окружения для текущей папки
(test_task_fileapi)$ pip install -U pip pipenv // установка утилиты для работы с зависимостями
(test_task_fileapi)$ pipenv install  // установка зависимостей проекта
(test_task_fileapi)$ pipenv install --dev // установка dev-зависимостей проекта
```

Важно: перед запуском внутри докера, нужно обязательно выполнить команду `pipenv install`, чтобы сформировался Pipfile.lock, именно из этого файла должна браться информация о зависимостях при сборке докер образа. Также необходимо добавить этот файл в git.

## Запуск внутри докера

```bash
$ docker-compose up
```

# Запуск тестов

```bash
export ENVIRONMENT=testing
$ python -m pytest -vvs
```

#TODO
1. Тесты
2. Docker
3. CI/CD
4. Flake8