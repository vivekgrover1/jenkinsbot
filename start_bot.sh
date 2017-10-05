#!/bin/sh
service mysql start
sleep 10
mysql -h "localhost" -u "root" "-psecretadmin" < "/docker-entrypoint-initdb.d/init.sql"
sleep 5
nohup python3.4 /root/bot/slackbot.py & 2>&1 >/dev/null
nohup python3.4 /root/bot/start_app.py & 2>&1 >/dev/null
pid1=`ps -ef | grep py | grep -v grep | grep "/root/bot/slackbot.py" | awk '{ print $2 }'`
pid2=`ps -ef | grep py | grep -v grep | grep "/root/bot/start_app.py" | awk '{ print $2 }'`
pid3=`ps -ef | grep mysql | grep -v grep | grep /usr/bin/mysqld_safe | awk '{ print $2 }'`
while [ ! -z "$pid1" -a ! -z "$pid2" -a ! -z "$pid3"]
do
sleep 200
pid1=`ps -ef | grep py | grep -v grep | grep "/root/bot/slackbot.py" | awk '{ print $2 }'`
pid2=`ps -ef | grep py | grep -v grep | grep "/root/bot/start_app.py" | awk '{ print $2 }'`
pid3=`ps -ef | grep mysql | grep -v grep | grep /usr/bin/mysqld_safe | awk '{ print $2 }'`
done
