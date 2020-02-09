# rest_tornado_sqlalchemy
- Сохраняет в базу данных:
    - полученный ЧИСЛОВОЙ массив
    - отсортироаванный массив чисел
    - дату создания записи
```
"request": {
    "method": "POST",
    "header": [
        {
            "key": "Content-Type",
            "name": "Content-Type",
            "value": "application/json",
            "type": "text"
        }
    ],
    "body": {
            }
        }
    },
    "url": {
        "raw": "http://localhost:8880/api/item/?Content-Type=application/json",
        "protocol": "http",
        "host": [
            "localhost"
        ],
        "port": "8880",
        "path": [
            "api",
            "item",
            ""
        ],
        "query": [
            {
                "key": "Content-Type",
                "value": "application/json"
            }
        ]
    },
    "description": "item"
}
```
- Возвращает отсортированный массив и дату записи

```
"request": {
    "method": "GET",
    "header": [],
    "url": {
        "raw": "http://localhost:3000/?Content-Type=application/json",
        "protocol": "http",
        "host": [
            "localhost"
        ],
        "port": "3000",
        "path": [
            ""
        ],
        "query": [
            {
                "key": "Content-Type",
                "value": "application/json"
            }
        ]
    },
    "description": "items"
}
```
Для локального запуска:
- установить Postgressql
- python 3.X
- создать таблицу
````
create table "table"
(
	id serial
		constraint table_pk
			primary key,
	raw_array int[] not null,
	sorted_array int[] not null,
	created_at date not null
);
````
Для запуска в docker:
- запустить docker-compose.yml

Установить зависимости из requrements.txt

Для тестирования:
- postman

Help:
- https://docs.sqlalchemy.org/en/13/orm/query.html
- https://tornado-sqlalchemy.readthedocs.io/en/latest/
- https://www.tornadoweb.org/en/stable/guide/coroutines.html
- https://hackersandslackers.com/database-queries-sqlalchemy-orm/