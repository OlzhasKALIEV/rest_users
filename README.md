# rest_users

Проект добавления пользователя в справочник. С предсказанием возраста и национальности по имени 

1. Клонирование проекта: git clone https://github.com/OlzhasKALIEV/rest_users.git
2. Переходим в проект: cd .\rest_users\
3. Создать файл .env в нем разместить информацию 

    API_AGIFY_URL=https://api.agify.io
   
    API_GENDERIZE_URL=https://api.genderize.io
   
    API_NATIONALIZE_URL=https://api.nationalize.io

    
    DATABASE_URL=postgresql://postgres:12345@localhost:5432/directory
   
    DATABASE_URL_IMG=postgresql://postgres:12345@db:5432/directory

   
    POSTGRES_USER=postgres

   
    POSTGRES_PASSWORD=12345

   
    POSTGRES_DB=directory
    
    PGADMIN_DEFAULT_EMAIL=admin@example.com
    PGADMIN_DEFAULT_PASSWORD=admin

5. Запуск проекта: docker-compose up

Создать пользователя

POST: http://0.0.0.0:8000/api/create/

JSON:
{
"name": "Dmitriy",
"surname": "Ushakov",
"patronymic": "Vasilevich"
}

![img.png](img/img_2.PNG)

Получение данных по id

GET: http://0.0.0.0:8000/api/users?id=1

![img.png](img/img_1.PNG)

Получение данных с различными фильтрами и пагинацией 

GET: http://0.0.0.0:8000/api/gender/male?age_min=25&age_max=80&page=1&limit=2

![img.png](img/img_11.PNG)

Удаления по идентификатору

DELETE: http://0.0.0.0:8000/api/users?id=1

![img.png](img/img_3.PNG)

Изменение данных по идентификатору

PUT: http://0.0.0.0:8000/api/users?id=2

JSON
{
    "name": "Новое имя пользователя",
    "surname": "Новая фамилия пользователя",
    "patronymic": "Новое отчество пользователя",
    "age": 25,
    "gender": "Мужской",
    "nationality": "RU"
}

![img.png](img/img_4.PNG)


Администрирование БД. Необходимо зайти войти в интерактивный pgAdmin: http://localhost:5050/login?next=%2F

Авторизоваться под администратором: 
    PGADMIN_DEFAULT_EMAIL=admin@example.com
    PGADMIN_DEFAULT_PASSWORD=admin

![img.png](img/img_5.PNG)

Зарегистрировать БД в pgAdmin

![img.png](img/img_6.PNG)

POSTGRES_USER=postgres
POSTGRES_PASSWORD=12345

![img.png](img/img_7.PNG)

![img.png](img/img_8.PNG)

Выполнить SQL запрос к таблице user_directory

![img.png](img/img_9.PNG)
