#!/bin/sh
echo "HI"
nohup python3.4 /root/bot/slackbot.py & 2>&1 >/dev/null
nohup python3.4 /root/bot/start_app.py & 2>&1 >/dev/null
echo "Hi"
