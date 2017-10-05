#!/bin/sh
echo "HI"
service mysql start
sleep 20
mysql -h "localhost" -u "root" "-psecretadmin" < "/docker-entrypoint-initdb.d/init.sql"
sleep 5
nohup python3.4 /root/bot/slackbot.py & 2>&1 >/dev/null

#python3.4 /root/bot/slackbot.py 
nohup python3.4 /root/bot/start_app.py & 2>&1 >/dev/null
sleep 500
echo "Hi"

