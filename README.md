# PyrogramBot-TestTask
Данный репозиторий содержит результат выполнения тестового задания на позицию Программист

## Условие
Воронка начинается после первого сообщения от клиента.
	
Пояснение: бот проверяет есть ли человек в БД, и если нет, то регистрирует его в БД и начинается воронка

Через какое время:	
Сообщения, которые отправляет с момента последнего

	1. через 10 минут	Добрый день!

	2. через 90 минут	Подготовила для вас материал

	3. Сразу после	Отправка любого фото

	4. Через 2 часа, если не найден в истории сообщений триггер "Хорошего дня" (от лица нашего аккаунта)
	Скоро вернусь с новым материалом!

ЯП -- python. Использовать sqlalchemy (asyncpg) - для БД, pyrogram - для взаимодействия с Telegram API. Логировать каждую успешную отправку сообщения с помощью loguru. Сделать возможность просмотра кол-во зарегистрированный людей в БД за сегодня с помощью отправки команды /users_today в избранное аккаунта.

## Преднастройки
1. Добавьте API_ID и API_HASH в ваш .env file (смотри .env_sample file)

2. Добавьте ваши настройки к базе данных PostgreSQL в database.ini file (смотри database_sample.ini)
```
[postgresql]
host=localhost
database=pyrogram_bot_db
user=pyrogram_bot_user
password=sample
port=5432
```
   
## Запуск через poetry:
1. Установить все зависимости
```
$ poetry install
```
2. Запустить бота 
```
$ poetry run python3.10 src/main.py
```
