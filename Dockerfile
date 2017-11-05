# Set the base image to vivek77/jenkinsbot
FROM vivek77/jenkins_slack_bot

# File Author / Maintainer
MAINTAINER Vivek

# Update the repository sources list
RUN apt-get -yqq update

WORKDIR /root/bot

COPY jenkins_bot_pickledb.py slack_cmd_process.py slack_message.py slackbot.py start_app.py /root/bot/

RUN chmod -R 755 /root/bot

RUN pip3.5 install tinydb

RUN rm -rf /var/lib/apt/lists/* && \
rm -rf /var/cache/apk/*

ENV PYTHONUNBUFFERED=0
