# Set the base image to vivek77/jenkinsbot
FROM vivek77/jenkinsbot

# File Author / Maintainer
MAINTAINER Vivek

# Update the repository sources list

RUN cd /root/bot;wget -Nq https://raw.githubusercontent.com/vivekgrover1/jenkinsbot/master/python_mysql.py && \
 wget -Nq https://raw.githubusercontent.com/vivekgrover1/jenkinsbot/master/slack_cmd_process.py && \
 wget -Nq https://raw.githubusercontent.com/vivekgrover1/jenkinsbot/master/slack_message.py && \
 wget -Nq https://raw.githubusercontent.com/vivekgrover1/jenkinsbot/master/slackbot.py && \
 wget -Nq https://raw.githubusercontent.com/vivekgrover1/jenkinsbot/master/start_app.py && \
 wget -Nq https://raw.githubusercontent.com/vivekgrover1/jenkinsbot/master/start_bot.sh


ENV SLACK_BOT_TOKEN="your_token" CHATBOT_NAME="your_bot_name" \
APPROVER_SLACK_NAME="APPROVER_SLACK_ID"

ENTRYPOINT /root/bot/start_bot.sh
