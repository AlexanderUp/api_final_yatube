# Описание yatube API

Инновационное приложение, позволяющее создавать публикации, читать публикации других авторов и подписываться на них - и все это через API.

## Запуск приложения:

- Клонируем репозиторий:

```git clone https://github.com/AlexanderUp/api_final_yatube.git```
    
- Переходим в папку проекта:

```cd api_final_yatube```

- Настраиваем виртуальное окружение:

```python3 -m pip venv venv```

- Активируем виртуальное окружение:

```source venv/bin/activate```

- Устанавливаем зависимости:

```python3 -m pip install -r requirements.txt```

- Переходим в папку проекта:

```cd yatube_api```

- Создаем и применяем миграции БД:

```python3 manage.py makemigrations```

```python3 manage.py migrate```

- Создаем суперпользователя, следуем инструкциям из терминала:

```python3 manage.py createsuperuser```

- Запускаем отладочный сервер:

```python3 manage.py runserver```

## Примеры запросов

- Получить список публикаций

```GET /api/v1/posts/```

- Создать публикацию

```POST /api/v1/posts/```

- Получить указанную публикацию по id

```GET /api/v1/posts/{id}/```

- Обновить полностью указанную публикацию по id

```PUT /api/v1/posts/{id}/```

- Обновить частично указанную публикацию по id

```PATCH /api/v1/posts/{id}/```

- Удалить указанную публикацию по id

```DELETE /api/v1/posts/{id}/```

- Получить список комментариев к посту

```GET /api/v1/posts/{post_id}/comments/```

- Создать комментарий к посту

```POST /api/v1/posts/{post_id}/comments/```

- Получить указанный комментарий по id

```GET api/v1/posts/{post_id}/comments/{id}/```

- Обновить полностью указанный комментарий по id

```PUT api/v1/posts/{post_id}/comments/{id}/```

- Обновить частично указанный комментарий по id

```PATCH api/v1/posts/{post_id}/comments/{id}/```

- Удалить указанный комментарий по id

```DELETE api/v1/posts/{post_id}/comments/{id}/```

- Получить список сообществ

```GET /api/v1/groups/```

- Получить информацию о указанном сообществе

```GET /api/v1/groups/{id}/```

- Получить список своих подписок

```GET /api/v1/follow/```

- Подписаться на пользователя по имени

```POST /api/v1/follow/```


## Использованные технологии

Django REST Framework 3.12.4

##  Об авторе

Автор - Уперенко Александр, студент 44 когорты Яндекс-Практикума направления Python-разработчик.
