### Описание проекта
Данный проект представляет собой часть будущего проекта социальной сети
и отвечает за интеграцию с другими проектами путем реализации 
программного интерфейса социальной сети.


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/k3llar/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

###  В сервисе реализована возможность получения и отправления публикаций, комментариев к ним,
### подписок на любимых авторов. Проверка прав доступа осуществляется через JWT токен.

Ниже приведены несколько операций с полученными ответами в формате JSON

Получение списка комментариев к записи
[GET]: http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/

```
EXAMPLE ANSWER
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```

Частичное обновление публикации
[PATCH]: http://127.0.0.1:8000/api/v1/posts/{id}/
```
EXAMPLE PAYLOAD
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

```
EXAMPLE ANSWER
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

#### Остальные пути и формы запросов расположены
[ALL_METHODS]: http://127.0.0.1:8000/redoc/
