
A simple messenger consisting of a JavaScript client and and a Django backend
# [JavaScript + Django Project Messenger](http://127.0.0.1:8000/accounts/login/)
## [Skillfactory](https://skillfactory.ru) FPW homework

Web-application example consisting of [JavaScript](https://devdocs.io/javascript/) frontend and [Django framework](https://docs.djangoproject.com/en/4.1/intro/install/) backend.
<hr>
<p> </p>

:arrow_down: [to Quick start](README.md#Quick-start)

<p> </p>

## Техническое задание и реализация  
<br>
Нам необходимо создать базовый мессенжер со следующими функциями:
<br>
- отправка и получение сообщений;

*Отправка и получение сообщений реализованы через [Channels Django](https://channels.readthedocs.io/en/stable/introduction.html) , которые устанавливают длительное соединение с пользователем по протоколу WebSockets.*

<br>
- создание, редактирование и удаление групповых чатов и переписка в них;

*Пользователь открывает свою комнату (Room) или присоединяется к действующим комнатам, которые основываются на технологии объединения Django Channels в группы Groups для обмена сообщениями между разными каналами.*

*Пользователи подключаются и выходят из комнат динамически, вход и выход обозначаются сообщением от пользователя.*

*Сообщения отправляются всем пользователям в комнате.*

*Сохранение сообщений для пользователей, покинувших комнату, не предусмотрено. При выходе всех пользователей из комнаты она становится недоступной.*

<br>
- редактирование личной информации пользователя (имя и аватар);

*Зарегистрированным пользователям доступна страница Профиль с возможностью добавления/редактирования имени, емейла, короткого текста о себе и аватара.*

<br>
- просмотр списка других пользователей с переходом на отправку им сообщений.

*Находясь в комнате чата пользователь видит динамический список других пользователей, подключенных к этой же комнате.*

*При выборе конкретного пользователя открывается форма для отправки личных сообщений. У получателя сообщения отображаются в общем чате с пометкой, что они персональные.*

<br>

### Quick start

Platform-depending options and libraries are adjusted to Windows.

Clone repository to ChatBoard_dir directory
```bash
git clone https://github.com/Dmitro-belous/Messenger
```

At ChatBoard_dir directory, start and adjust virtual environment
```bash
python -m venv venv
venv\scripts\activate
cd django_messenger 
pip install -r requirements.txt
```

Generate Django secret-key
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

At the inner django_messenger directory (project dir) add venv/settings.env file for private settings 
```python
SECRET_KEY = ''
```

Mark ChatBoard directory as Sources root

Create superuser
```
python manage.py createsuperuser
```
You also have to use Docker to install and run Redis. I use Redis as the backing store for the channel layer. [Install Docker](https://www.docker.com/products/docker-desktop/) from its official website - there are official runtimes for Windows that make it easy to use.

To start a Redis server on port 6379, run the following command
```bash
docker run --rm -p 6379:6379 redis:7
```

Open a second terminal and start server
```bash
python manage.py runserver
```

Main page works at url http://127.0.0.1:8000/ - local host that server advises you at start message

[Messenger](http://127.0.0.1:8000/)
<p> </p>
<p> </p>

:arrow_up: [to begin](README.md#Техническое-задание-и-реализация)
