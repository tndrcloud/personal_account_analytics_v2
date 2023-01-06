<h2>Анализатор ЛК ВАТС</h2>

 REST API сервис для аналитики ЛК ВАТС

<h2>Requirements</h2>

 - Python 3.8+
 - FastAPI
 - PostgreSQL
 - Uvicorn

 Используйте команду *pip3 install -r src\requirements.txt* для установки необходимых пакетов

 Если pip3 не установлен: *sudo apt-install python3-pip*

<h2>Как использовать</h2>
 
Если вы запускаете программу из командной строки, запустите ее как sudo-user (root)
 
If you run programm like a service check yourself.
 
**Для запуска этой программы/скрипта вы можете использовать следующие команды:**
 
- Запуск с открытой консолью. Не удается использовать консоль для других задач (консоль недоступна):

  *python3 /path/to/script/__main__.py*

- Запуск с открытой консолью. Можете использовать консоль для других задач (консоль доступна):

  *python3 /path/to/script/__main__.py &*

- Запуск как daemon. Консоль может использоваться для других задач или может быть закрыта:

1. Создайте daemon-файл *sudo touch /etc/systemd/system/account_analytics.service*
2. Напишите следующее в созданный daemon-файл:

  <code>

     [Unit]
      Description=Telegram bot
      After=multi-user.target

     [Service]
      Type=idle
      ExecStart=/usr/bin/python3 /path/to/script/bot.py
      Restart=always

     [Install]
      WantedBy=multi-user.target </code>

  
    
3. Теперь запустите daemon выполняя команды последовательно:
  
 - *sudo systemctl daemon-reload*
 - *sudo systemctl enable account_analytics.service*
 - *sudo systemctl start account_analytics.service*
