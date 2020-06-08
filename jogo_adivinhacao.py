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
				"text": "Hora da charada!! :grinning: :"
			}
    }
    DIVIDER_BLOCK = {"type": "divider"}


    QUESTION_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "<text>",
        }
    }

    adivinhacao = ""

    def __init__(self, channel):       

        self.adivinhacao = jgAdivinhacao.comeca_jogo()

        self.channel = channel
        self.username = "Synergy-Bot"
        self.timestamp = ""
        self.reaction_task_completed = False
        self.pin_task_completed = False

    def get_message_payload(self):
        self.QUESTION_BLOCK["text"]["text"] = self.QUESTION_BLOCK["text"]["text"].replace("<text>", self.adivinhacao["pergunta"])
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "blocks": [
                self.TITLE_BLOCK,
                self.DIVIDER_BLOCK,
                self.QUESTION_BLOCK
            ],
        }
    
    CORRECT_BLOCK = {
		
            "type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "ACERTOU, PARABENS :grinning:"
			}
    }
    
    WRONG_BLOCK = {
		
            "type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Errado! :no_mouth:"
			}
    }

    def get_message_ingame(self, text):
        if text == self.adivinhacao["resposta"]:
            return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "blocks": [
                self.CORRECT_BLOCK
            ],
        }
        else:
            return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "blocks": [
                self.WRONG_BLOCK
            ],
        }

    def get_is_correct(self, text):
        if text == self.adivinhacao["resposta"]:
            return True
        else:
            return False
    
    def get_dica(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "blocks": [
                {		
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": self.adivinhacao["dica"]
                        }
                }
            ],
        }
        