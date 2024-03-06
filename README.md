# testovoe-zadanie-brandgames
Загрузка рандомных изображений собак
В базе данных сохраняются пользователи (id, username) и изображения (id, дата создания, id пользователя)
## Как запустить:
###Установить виртуальное окружение:
```
python -m venv venv
venv\scripts\activate
```
Зависимости:
```
pip install django aiogram
или
pip install -r requirements.txt
```
Джанго проект:
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
Запустить бота
```
python manage.py bot.py
```
Перейти в чат к боту и нажать кнопку грузить собаку
https://t.me/dog_aiogram_bot
