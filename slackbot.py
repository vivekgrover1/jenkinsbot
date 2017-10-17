import os
import time
import subprocess
from slackclient import SlackClient
import slack_cmd_process
import threading
import python_mysql
import slack_message


# return username of the user
def get_user_name(username, slack_client):
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('id') == username:
                return user.get('name')


# return bot_id of the user
def get_bot_id(bot_name, slack_client):
    """
        This function gets the id of bot based on its name in slack team.
        We need the id because it allows us to parse the message directed at bot.

    """
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == bot_name:
                return user.get('id')


def get_im_id(user_id, slack_client):
    """
        This function gets the id of bot based on its name in slack team.
        We need the id because it allows us to parse the message directed at bot.

    """
    api_call = slack_client.api_call("im.list")
    if api_call.get('ok'):
        ims = api_call.get('ims')
        for user in ims:
            if 'user' in user and user.get('user') == user_id:
                return user.get('id')


def handle_command(command, channel, msg_id, user_id):
    """
        Receives commands directed at the bot and sends to function cmd_process
        to process the command , which returns the response. Based on response it post the
        message to slack thread or message.
    """
    username = get_user_name(user_id, slack_client)
    python_mysql.add_user(username)

    if command == "member joined":
        msg = ":slack: Welcome to the channel, Here you can instruct the jenkinsbot to execute the job based on the " \
              "id.\n\nYou can use @jenkinsbot help message to get the usage details.\n\nPlease note you need to get " \
              "the Approval from Admin for every job that you will execute. "
        python_mysql.add_user(username)
        slack_message.send_message_without_button(username, msg, channel)
    else:

        response, status, color, job_id = slack_cmd_process.cmd_process(command, username,channel)
        if status != "notapproved":
            if msg_id == "Thread_False":
                slack_client.api_call("chat.postMessage", channel=channel,
                                      text="<@%s> " % user_id, as_user=True,
                                      attachments=[{"text": "%s" % response, "color": "%s" % color}])
            else:
                slack_client.api_call("chat.postMessage", channel=channel,
                                      text="<@%s> " % user_id, as_user=True, thread_ts=msg_id,
                                      attachments=[{"text": "%s" % response, "color": "%s" % color}])

        else:
            slack_client.api_call("chat.postMessage", channel=channel,
                                  text="<@%s> " % user_id, as_user=True, attachments=[
                    {"text": "%s" % response, "color": "%s" % color, "attachment_type": "default",
                     "callback_id": "{0}_{1}_{2}".format(username, job_id, channel),
                     "actions": [{"name": "option", "text": "Send it in!", "type": "button", "value": "Yes"}, {
                         "name": "no",
                         "text": "Not now, may be later!",
                         "type": "button",
                         "value": "bad"
                     }]}])


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function parse the message directed at bot based on its id
        and return None otherwise.
    """
    output_list = slack_rtm_output

    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text'] and 'thread_ts' in output:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel'], output['thread_ts'], output['user']
            elif output and 'text' in output and AT_BOT in output['text']:
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel'], "Thread_False", output['user']
            elif output and 'type' in output and 'member_joined_channel' in output['type']:
                return "member joined", output['channel'], "Thread_False", output['user']

    return None, None, None, None


def process_slack_output(cmd, chn, msg, usr):
    """
        Message directed at bot is created into thread , to speed up the
        processing of the message.
    """

    t = threading.Thread(target=handle_command, args=(cmd, chn, msg, usr,))
    threads.append(t)
    t.start()


if __name__ == "__main__":

    slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
    BOT_NAME = os.environ.get('CHATBOT_NAME')
    BOT_ID = get_bot_id(BOT_NAME, slack_client)
    AT_BOT = "<@" + BOT_ID + ">"
    threads = []

    WEBSOCKET_DELAY = 1  # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            sc = slack_client.rtm_read()
            command, channel, msg_id, user_id = parse_slack_output(sc)
            if command and channel and msg_id and user_id:
                process_slack_output(command, channel, msg_id, user_id)
            time.sleep(WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
