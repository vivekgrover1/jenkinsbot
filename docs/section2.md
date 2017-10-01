## Section 2: Subscribe to Events

Once you have created the Slack App and Bot User, let's have it subscribe to some events in Slack!

On your app's settings page you'll find **Event Subscriptions** on the left navigation bar.

Near the bottom of the page under the **WorkSpace Events** section you'll be able to subscribe your bot to the events.

![add_WorkSpace_events](https://s3.ap-south-1.amazonaws.com/jenkinsbot/events.PNG)

This project uses the following events:

- [message.channels](https://api.slack.com/events/message.channels)
- [message.im](https://api.slack.com/events/message.im)

After you've subscribed to all the events your app will need, you need to enable the interactive components.

On your app's settings page you'll find **Interactive Components** on the left navigation bar.

Click on button Enable Inteactive Components and Add the URL like below:

http://HOST:PORT_NO/slack/message_actions (Select the post of your machine which you want to expose)

![Enable Inteactive Components](https://s3.ap-south-1.amazonaws.com/jenkinsbot/events2.PNG)

When you are done, make sure to **Save Changes**.

---
**Next [Section 4:  App Credentials](./../docs/Section-4.md)**  
**Previous [Section 2: Create a Slack App and Bot User](./../docs/Section-2.md)**  
