import random 

class Conversa:
    """Constructs the onboarding message and stores the state of which tasks were completed."""

    conversas = [
    "Qual seu filme favorito?",
    "Quais séries ou filmes vocês tem assistido atualmente?",
    "Três momentos marcantes da sua vida",
    "O que você faz quando está tendo um dia ruim?",
    "Quem é uma inspiração para você?",
    ]

    TITLE_MESSAGE = {
		
            "type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "O Assunto para conversarmos é:"
			}
    }
    DIVIDER_BLOCK = {"type": "divider"}


    CONVERSA_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "<text>",
        }
    }
    def __init__(self, channel):
        self.channel = channel
        self.username = "Synergy-Bot"
        self.timestamp = ""

    def get_message_payload(self):
        num = random.randint(0, len(self.conversas)-1)
        self.CONVERSA_BLOCK["text"]["text"] = self.CONVERSA_BLOCK["text"]["text"].replace("<text>", self.conversas[num])
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "blocks": [
                self.TITLE_MESSAGE,
                self.DIVIDER_BLOCK,
                self.CONVERSA_BLOCK
            ],
        }
