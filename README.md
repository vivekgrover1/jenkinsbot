# JenkinsSlack Bot
## Deploying a JenkinsSlack bot using [Docker Container](https://github.com/vivekgrover1/jenkinsbot/blob/master/Dockerfile) 
This bot is an implementation of CI/CD Process Integration with ChatOps and building a Slack App with Slack's Python SDK, [python-slackclient](http://python-slackclient.readthedocs.io/en/latest/).

We'll cover all the steps you'll need to configure and deploy JenkinsSlack Bot to your Slack Workspace.

JenkinsSlack Bot is designed to help DevOps engineers to execute the CI/CD Process from the chatroom. Additionally, In order to have control over unauthorized deployment of code to different application environment, there is authorization mechanism so that only approved commands can trigger the deployment. 

>![JenkinsSlackbot](https://s3.ap-south-1.amazonaws.com/jenkinsbot/ezgif.com-optimize.gif)

Let's start with the jenkinsSlack bot :sparkles:

* [Section 1: Create a Slack App and Bot User](docs/section1.md)  
* [Section 2: Subscribe to Events and Enable Interactive Components](docs/section2.md)  
* [Section 3: Install Slack App](docs/section3.md)


### Specify the Environment Variable in docker file.

```
ENV SLACK_BOT_TOKEN="slack-token" CHATBOT_NAME="your_bot_name" \
APPROVER_SLACK_NAME="SLACK_USER_ID" 

```


### Building the bot from docker file.

```
docker build -t jenkinsbot .

```
### Run the container with --publish option in run command.

```
 docker run -d -p 98:80 -it --name jenkinsbot jenkinsbot
 
 docker exec jenkinsbot sh /root/bot/start_bot.sh

```
