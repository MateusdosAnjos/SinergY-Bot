import os
import logging
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from onboarding_tutorial import OnboardingTutorial
from help_info import HelpInfo
from join_channel import JoinChannel
from jogo_adivinhacao import JogoAdivinhacao
from conversa import Conversa

# Initialize a Flask app to host the events adapter
app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(os.environ["SLACK_SIGNING_SECRET"], "/slack/events", app)

# Initialize a Web API client
slack_web_client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

# For simplicity we'll store our app data in-memory with the following data structure.
# onboarding_tutorials_sent = {"channel": {"user_id": OnboardingTutorial}}
onboarding_tutorials_sent = {}
help_info_sent = {}
join_channel_sent = {}
jogo_adivinhacao_sent = {}
conversa_sent = {}

ingame = False
dica_time = False
should_join = False
jogo_adivinhacao =  ""

#START MESSAGE
def start_onboarding(user_id: str, channel: str):
    # Create a new onboarding tutorial.
    onboarding_tutorial = OnboardingTutorial(channel)

    # Get the onboarding message payload
    message = onboarding_tutorial.get_message_payload()

    # Post the onboarding message in Slack
    response = slack_web_client.chat_postMessage(**message)

    # Capture the timestamp of the message we've just posted so
    # we can use it to update the message after a user
    # has completed an onboarding task.
    onboarding_tutorial.timestamp = response["ts"]

    # Store the message sent in onboarding_tutorials_sent
    if channel not in onboarding_tutorials_sent:
        onboarding_tutorials_sent[channel] = {}
    onboarding_tutorials_sent[channel][user_id] = onboarding_tutorial

## HELPER METHOD!
def show_help_info(user_id: str, channel: str):
    # Create a new info helper.
    help_info = HelpInfo(channel)

    # Get the onboarding message payload
    message = help_info.get_message_payload()

    # Post the onboarding message in Slack
    response = slack_web_client.chat_postMessage(**message)

    # Capture the timestamp of the message we've just posted so
    # we can use it to update the message after a user
    # has completed an onboarding task.
    help_info.timestamp = response["ts"]

    # Store the message sent in help_info_sent
    if channel not in help_info_sent:
        help_info_sent[channel] = {}
    help_info_sent[channel][user_id] = help_info

## PUXA CARTA OPERATIONS!
def show_conversa(user_id: str, channel: str):
    # Create a new info helper.
    conversa = Conversa(channel)

    # Get the onboarding message payload
    message = conversa.get_message_payload()

    # Post the onboarding message in Slack
    response = slack_web_client.chat_postMessage(**message)

    # Capture the timestamp of the message we've just posted so
    # we can use it to update the message after a user
    # has completed an onboarding task.
    conversa.timestamp = response["ts"]

    # Store the message sent in conversa_sent
    if channel not in conversa_sent:
        conversa_sent[channel] = {}
    conversa_sent[channel][user_id] = conversa


## JOIN CHANNEL OPERATIONS!
def join_channel(user_id: str, channel: str):
    # Create a new join channel.
    join_channel = JoinChannel(channel)

    # Get the onboarding message payload
    message = join_channel.get_message_payload()

    # Post the onboarding message in Slack
    response = slack_web_client.chat_postMessage(**message)

    # Capture the timestamp of the message we've just posted so
    # we can use it to update the message after a user
    # has completed an onboarding task.
    join_channel.timestamp = response["ts"]

    # Store the message sent in join_channel_sent
    if channel not in join_channel_sent:
        join_channel_sent[channel] = {}
    join_channel_sent[channel][user_id] = join_channel


def channel_to_join(user_id: str, channel: str, channel_name: str):
    test = slack_web_client.conversations_list()
    for dic in test['channels']:
        if dic['name'] == channel_name:
            channel_id = dic['id']
            break

    if channel_name:
        response = slack_web_client.conversations_join(channel=channel_id)
    
    return start_onboarding(user_id, channel_id)

## RIDDLE GAME OPERATIONS!    
def riddle_game(user_id: str, channel: str):
    global jogo_adivinhacao
    # Create a new join channel.
    jogo_adivinhacao = JogoAdivinhacao(channel)

    # Get the onboarding message payload
    message = jogo_adivinhacao.get_message_payload()

    # Post the onboarding message in Slack
    response = slack_web_client.chat_postMessage(**message)

    # Capture the timestamp of the message we've just posted so
    # we can use it to update the message after a user
    # has completed an onboarding task.
    jogo_adivinhacao.timestamp = response["ts"]

    # Store the message sent in join_channel_sent
    if channel not in jogo_adivinhacao_sent:
        jogo_adivinhacao_sent[channel] = {}
    jogo_adivinhacao_sent[channel][user_id] = jogo_adivinhacao

def ingame_riddle(user_id: str, channel: str, text: str):
    # Get the onboarding message payload

    # response = slack_web_client.users_info(user=user_id)
    # user_name = response["user"]["real_name"]    

    message = jogo_adivinhacao.get_message_ingame(text, user_id)

    global ingame
    global dica_time

    if text.lower() == "dica":
        dica_time = True
        message = jogo_adivinhacao.get_dica()
    elif jogo_adivinhacao.get_is_correct(text):
        ingame = False
    else:
        ingame = True

    # Post the onboarding message in Slack
    response = slack_web_client.chat_postMessage(**message)

    # Capture the timestamp of the message we've just posted so
    # we can use it to update the message after a user
    # has completed an onboarding task.
    jogo_adivinhacao.timestamp = response["ts"]

    # Store the message sent in join_channel_sent
    if channel not in jogo_adivinhacao_sent:
        jogo_adivinhacao_sent[channel] = {}
    jogo_adivinhacao_sent[channel][user_id] = jogo_adivinhacao

    return ingame

# ================ Team Join Event =============== #
# When the user first joins a team, the type of the event will be 'team_join'.
# Here we'll link the onboarding_message callback to the 'team_join' event.
@slack_events_adapter.on("team_join")
def onboarding_message(payload):
    """Create and send an onboarding welcome message to new users. Save the
    time stamp of this message so we can update this message in the future.
    """
    event = payload.get("event", {})

    # Get the id of the Slack user associated with the incoming event
    user_id = event.get("user", {}).get("id")

    # Open a DM with the new user.
    response = slack_web_client.im_open(user=user_id)
    channel = response["channel"]["id"]

    # Post the onboarding message.
    start_onboarding(user_id, channel)


# ============= Reaction Added Events ============= #
# When a users adds an emoji reaction to the onboarding message,
# the type of the event will be 'reaction_added'.
# Here we'll link the update_emoji callback to the 'reaction_added' event.
@slack_events_adapter.on("reaction_added")
def update_emoji(payload):
    """Update the onboarding welcome message after receiving a "reaction_added"
    event from Slack. Update timestamp for welcome message as well.
    """
    event = payload.get("event", {})

    channel_id = event.get("item", {}).get("channel")
    user_id = event.get("user")

    if channel_id not in onboarding_tutorials_sent:
        return

    # Get the original tutorial sent.
    onboarding_tutorial = onboarding_tutorials_sent[channel_id][user_id]

    # Mark the reaction task as completed.
    onboarding_tutorial.reaction_task_completed = True

    # Get the new message payload
    message = onboarding_tutorial.get_message_payload()

    # Post the updated message in Slack
    updated_message = slack_web_client.chat_update(**message)

    # Update the timestamp saved on the onboarding tutorial object
    onboarding_tutorial.timestamp = updated_message["ts"]


# =============== Pin Added Events ================ #
# When a users pins a message the type of the event will be 'pin_added'.
# Here we'll link the update_pin callback to the 'reaction_added' event.
@slack_events_adapter.on("pin_added")
def update_pin(payload):
    """Update the onboarding welcome message after receiving a "pin_added"
    event from Slack. Update timestamp for welcome message as well.
    """
    event = payload.get("event", {})

    channel_id = event.get("channel_id")
    user_id = event.get("user")

    # Get the original tutorial sent.
    onboarding_tutorial = onboarding_tutorials_sent[channel_id][user_id]

    # Mark the pin task as completed.
    onboarding_tutorial.pin_task_completed = True

    # Get the new message payload
    message = onboarding_tutorial.get_message_payload()

    # Post the updated message in Slack
    updated_message = slack_web_client.chat_update(**message)

    # Update the timestamp saved on the onboarding tutorial object
    onboarding_tutorial.timestamp = updated_message["ts"]

# ============== Message Events ============= #
# When a user sends a DM, the event type will be 'message'.
# Here we'll link the message callback to the 'message' event.
@slack_events_adapter.on("message")
def message(payload):
    """Display the onboarding welcome message after receiving a message
    that contains "start".
    """
    event = payload.get("event", {})

    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")

    global ingame
    global should_join
    global dica_time

    #IGNORES THE BOT MESSAGE
    if text == "This content can't be displayed.":
        return

    # STOPS THE GAMEPLAY
    if text.lower() == "end_game":
        ingame = False
        return

    #USERS ARE INGAME   
    if ingame and not dica_time:
        if ingame_riddle(user_id, channel_id, text):
            ingame = False
        return

    #ENDS DICA TIME
    dica_time = False


    # THE BOT IS EXPECTING A CHANNEL NAME TO JOIN!
    if should_join:
        should_join = False
        return channel_to_join(user_id, channel_id, text)

    # VERIFICATION OF TEXT (AVOID CRASHES)
    if text == None:
        return 
    
    # THE COMMANDS THE BOT ACCEPTS
    if text.lower() == "start":
        return start_onboarding(user_id, channel_id)
    
    elif text.lower() == "info" or text.lower() == "help":
        return show_help_info(user_id, channel_id)

    elif text.lower() == "join":
        should_join = True
        return join_channel(user_id, channel_id)
        
    elif text.lower() == "jogo_charada":
        ingame = True
        return riddle_game(user_id, channel_id)
    
    elif text.lower() == "conversa":
        return show_conversa(user_id, channel_id)


@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
    emoji = event_data["event"]["reaction"]
    print(emoji)

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    app.run(port=3000)
