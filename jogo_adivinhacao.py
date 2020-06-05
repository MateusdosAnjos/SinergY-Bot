import base_jogo_adivinhacao as jgAdivinhacao 

class JogoAdivinhacao:
    adivinhacao = {
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


    def __init__(self, channel):       

        adivinhacao = jgAdivinhacao.comeca_jogo()

        QUESTION_BLOCK = {
            "type": "section",
			"text": {
				"type": "mrkdwn",
				# "text": f"{adivinhacao["pergunta"]}"
                "text": "teste de texto",
			}
        }
        self.channel = channel
        self.username = "Synergy-Bot"
        self.icon_emoji = ":robot_face:"
        self.timestamp = ""
        self.reaction_task_completed = False
        self.pin_task_completed = False

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

    