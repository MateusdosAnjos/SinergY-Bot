import base_jogo_advinhacao as jgAdvinhacao 

class JogoAdivinhacao:
    advinhacao = {
        "pergunta" : "",
        "resposta" : "",
        "dica" : ""
    }

    TITLE_BLOCK = {
		
            "type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Hora da adivinhação :grinning: :"
			}
    }
    DIVIDER_BLOCK = {"type": "divider"}
    QUESTION_BLOCK 


    def __init__(self, channel):       

        advinhacao = jgAdvinhacao.comeca_jogo()

        QUESTION_BLOCK = {
            "type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"{advinhacao["pergunta"]} "
			}
        }
        self.channel = channel
        self.username = "pythonboardingbot"
        self.icon_emoji = ":robot_face:"
        self.timestamp = ""
        self.reaction_task_completed = False
        self.pin_task_completed = False

    }

    def get_message_payload(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.WELCOME_BLOCK,
                self.DIVIDER_BLOCK,
                self.QUESTION_BLOCK
            ],
        }

    