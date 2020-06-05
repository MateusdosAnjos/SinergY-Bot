class JoinChannel:
    """Constructs the join channel."""

    TITLE_MESSAGE = {	
            "type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Em qual channel devo me conectar?"
			}
    }

    def __init__(self, channel):
        self.channel = channel
        self.username = "Synergy-Bot"
        self.timestamp = ""

    def get_message_payload(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "blocks": [
                self.TITLE_MESSAGE,
            ],
        }
