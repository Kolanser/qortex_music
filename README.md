# Qortex Music

![](https://static-s.aa-cdn.net/img/gp/20600000632187/emMVz-GsPzDHtBLNTRmORAsEWPYt9LTAivnrBRNtuYHP4IQrgkPb22hl1UqGHu_zBJU?v=1)

### Технологии:

- Python

- Django

- Django Rest Framework API

- Gunicorn

- Docker

- Docker Compose



 

### _Описание_

Qortex Music - это каталог исполнителей и их альбомов с песнями такой структуры:

-   Исполнитель
    -   Название
-   Альбом
    -   Исполнитель
    - Название альбома
    -   Год выпуска
-   Песня
    -   Название
    -   Порядковый номер в альбоме

Одна и та же песня может быть включена в несколько альбомов, но под разными порядковыми номерами.

   

###  Для запуска проекта необходимо:.


Клонировать репозиторий и перейти в него в командной строке:

```sh
git clone git@github.com:Kolanser/qortex_music.git
cd qortex_music
```
Далее проект необходимо запустить через ***docker compose***. Взлетаем!:
```sh
docker-compose up -d
```
Для выполнения миграция и создания БД:
```sh
docker-compose exec web python manage.py migrate
```
Для создания суперпользователя, используйте:
```sh
docker compose exec backend python manage.py createsuperuser
```
Соберите статические файлы в единое место (--no-input - без запроса параметров у пользователя):
```sh
docker compose exec web python manage.py collectstatic --no-input

```
Для остановки работы контейнера, удаления его и томов используйте:

```sh
docker-compose down -v
```
### Актуальная информация по взаимодействию с эндпоинтами
Для быстрого ориентирования в системе эндпоинтов API в проекте подключена документация API. Воспользоваться ей можно пройдя по адресу:

```sh
http://127.0.0.1/swagger/
```

  

В ней описаны возможные запросы к API и структура ожидаемых ответов.

  

  

### Автор

  

  

[**Николай Слесарев**](https://github.com/Kolanser)