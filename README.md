# yatube API
Инновационное приложение, позволяющее создавать посты, читать посты других авторов и подписываться на них - и все это через API.

## Запуск приложения в режиме отладки:

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

