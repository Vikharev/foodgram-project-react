# praktikum_new_diplom

### Foodgram - «Продуктовый помощник»
Foodgram - сервис для просмотра и публикации рецептов

Возможности сервиса:
- Создать свой профиль
- Создавать и публиковать рецепты на основе имеющихся в базе даных ингредиентов
- Указывать теги для своих рецептов
- Загружать изображения своих рецептов
- Просматривать рецепты других пользователей
- Добавлять рецепты в избранное
- Добавлять рецепты в корзину
- Формировать список покупок (список ингредиентов с количеством) из рецептов в корзине
- Подписываться на других пользователей
- Фильтровать рецепты по тегам

## Как развернуть проект на сервере:

Клонировать репозиторий:
```
git@github.com:Vikharev/foodgram-project-react.git
```

Установить на сервере Docker, Docker Compose:

```
sudo apt install curl    
curl -fsSL https://get.docker.com -o get-docker.sh 
sh get-docker.sh                                   
sudo apt-get install docker-compose-plugin       
```

Скопировать на сервер файлы docker-compose.yml, nginx.conf из папки infra (команды выполнять находясь в папке infra):

```
scp docker-compose.yml nginx.conf <имя пользователя на сервере>@<публичный IP сервера>:/home/<username>/  
```

Создать файл .env и заполнить своими данными:
```
touch .env
nano .env
```
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432

SECRET_KEY=ключ Django-приложения
```

Создать и запустить контейнеры Docker, выполнить команду на сервере
*(версии команд "docker compose" или "docker-compose" отличаются в зависимости от установленной версии Docker Compose):*
```
sudo docker compose up -d
```

После успешной сборки выполнить миграции:
```
sudo docker compose exec backend python manage.py makemigrations
sudo docker compose exec backend python manage.py migrate
```

Создать суперпользователя:
```
sudo docker compose exec backend python manage.py createsuperuser
```

Собрать статику:
```
sudo docker compose exec backend python manage.py collectstatic --noinput
```

Наполнить базу данных содержимым из дампа ingredients.json:
```
sudo docker compose exec backend python manage.py loaddata ingredients.json
```

### Автор

**Вихарев Алексей**

[![Django-app workflow](https://github.com/vikharev/foodgram-project-react/actions/workflows/main.yml/badge.svg)](https://github.com/vikharev/foodgram-project-react/actions/workflows/main.yml)