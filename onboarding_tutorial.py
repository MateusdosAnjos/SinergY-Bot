class OnboardingTutorial:
    """Constructs the onboarding message and stores the state of which tasks were completed."""

    WELCOME_BLOCK = {
		
            "type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Bora dar uma energizada? :zap::zap::zap:"
			}
    }
    DIVIDER_BLOCK = {"type": "divider"}
    HELP_BLOCK = {
		
            "type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Digite 'info' para ver as opções"
			}
    }

    BUTTON = {
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Click Me",
						"emoji": True
					},
					"value": "click_me_123"
				}
			]
		}

    def __init__(self, channel):
        self.channel = channel
        self.username = "Synergy-Bot"
        self.timestamp = ""
        self.reaction_task_completed = False
        self.pin_task_completed = False

    def get_message_payload(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "blocks": [
                self.WELCOME_BLOCK,
                self.DIVIDER_BLOCK,
                self.HELP_BLOCK,
                self.BUTTON
            ],
        }
