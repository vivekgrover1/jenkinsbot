#!/usr/bin/bash
nohup python3.4 slackbot.py & 2>&1 >/dev/null
nohup python3.4 start_app.py & 2>&1 >/dev/null
