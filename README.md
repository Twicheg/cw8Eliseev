## healthy-habit-tracker+Docker

***

### Контекст

В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и
искоренению старых плохих привычек. Заказчик прочитал книгу, впечатлился и обратился к вам с запросом реализовать трекер
полезных привычек.

### Настройка удаленного сервера:
- скопировать весь проект на удаленный сервер
- убедиться что в файле .env DOCKER=1
- В файле имена базы данных POSTGRES_DB и DB_NAME должны совпадать
- POSTGRES_PASSWORD задает пароль , DB_PASSWORD пароль для входа
- SERVER_IP внешний адрес сервера
- DB_HOST названия сервера в докер-композе
- настроить Nginx
- выполнисть docker-compose up --build

### Задачи:

Настроили CORS.\
Настроили интеграцию с Telegram.\
Реализовали пагинацию.\
Использовали переменные окружения.\
Все необходимые модели описаны или переопределены.\
Все необходимые эндпоинты реализовали.\
Настроили все необходимые валидаторы.\
Описанные права доступа заложены.\
Настроили отложенную задачу через Celery.\
Проект покрыли тестами как минимум на 80%.\
Код оформили в соответствии с лучшими практиками.\
Имеется список зависимостей.\
Результат проверки Flake8 равен 100%, при исключении миграций.\
Решение выложили на GitHub.
***

### Эндпоинты:

#### Регистрация *api/users/create

#### Авторизация *api/token/

#### Список привычек текущего пользователя с пагинацией *api/habit/

#### Список публичных привычек  *api/habit/public

#### Создание привычки *api/habit/create/

#### Редактирование привычки *habit/update/id/

#### Удаление привычки *habit/delete/id/

### К созданию/редактированию/просмотру/удалению привычки имеют доступ только авторизированные пользователи

### Вывод списка привычек идет по 5 на страницу

## При создании привычки:

###  * необходимо указывать какая это привычка, связанная или полезная

###  * Нельзя указывать время на привычку более 120 секунд

###  * Привычка не может быть связанной и полезной одновременно

###  * Вознаграждение может быть только у приятной привычки

###  * Нельзя выполнять привычку реже, чем 1 раз в 7 дней.

## При создании пользователя:

###  * необходимо указывать mail,password и информацию телеграмма (опционально: id пользователя и обязательно: nickname)

### Чтобы бот начал присылать напоминания, необходимо ему написать в чат, ссылка на бота <link>

## Документация:

### /redoc

### /docs
# cw8Eliseev
