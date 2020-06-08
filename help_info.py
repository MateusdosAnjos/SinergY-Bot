class HelpInfo:
    """Constructs the onboarding message and stores the state of which tasks were completed."""

    TITLE_MESSAGE = {
		
            "type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "As opções de energizer são:"
			}
    }
    OPTION_1 = {
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Digite 'start' para iniciar o bot",
				"emoji": True
			}
		}
    OPTION_2 = {
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Digite 'help' ou 'info' para ver o menu de ajuda",
				"emoji": True
			}
		}
    OPTION_3 = {
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Digite 'join' para escolher qual canal devo me conectar",
				"emoji": True
			}
		}
    OPTION_4 = {
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Digite 'jogo_charada' para jogar o jogo",
				"emoji": True
			}
		}

    OPTION_5 = {
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Digite 'conversa' para obter um tema de conversa",
				"emoji": True
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
                self.OPTION_1,
                self.OPTION_2,
                self.OPTION_3,
                self.OPTION_4,
				self.OPTION_5,
            ],
        }
