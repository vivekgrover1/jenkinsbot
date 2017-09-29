# Set the base image to mysql
FROM mysql

# File Author / Maintainer
MAINTAINER  Vivek

# Update the repository sources list
RUN apt-get update && apt-get install vim -y && apt-get install wget -y
RUN mkdir /root/bot
RUN cd /root/bot;wget https://raw.githubusercontent.com/vivekgrover1/jenkinsbot/master/python_mysql.py && \
 wget https://raw.githubusercontent.com/vivekgrover1/jenkinsbot/master/slack_cmd_process.py && \
 wget https://raw.githubusercontent.com/vivekgrover1/jenkinsbot/master/slack_message.py && \
 wget https://raw.githubusercontent.com/vivekgrover1/jenkinsbot/master/slackbot.py && \
 wget https://raw.githubusercontent.com/vivekgrover1/jenkinsbot/master/start_app.py

ENV SLACK_BOT_TOKEN "xoxb-247103507941-IFG9viTV4sSJR4Ul0mUmSRee"
ENV CHATBOT_NAME "jenkinsbot"
ENV EC2_HOST "ec2-35-154-129-12.ap-south-1.compute.amazonaws.com"
ENV USER_PASS "vivek"

ADD init.sql /docker-entrypoint-initdb.d
RUN chmod 777 /docker-entrypoint-initdb.d/init.sql

ENV MYSQL_ROOT_PASSWORD secretadmin

RUN apt-get install python3 -y && apt-get install python3-setuptools -y &&  easy_install3 pip

RUN pip3.4 install slackclient && pip3.4 install pymysql && pip3.4 install python-jenkins && pip3.4 install flask
