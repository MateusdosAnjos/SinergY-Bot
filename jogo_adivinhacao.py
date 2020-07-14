import base_jogo_adivinhacao as jgAdivinhacao 
import random

class JogoAdivinhacao:
    
    adivinhacao = {
        "pergunta" : "",
        "resposta" : [],
        "dica" : ""
    }

    TITLE_BLOCK = {
		
            "type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Hora da charada!! :grinning:"
			}
    }
    DIVIDER_BLOCK = {"type": "divider"}

    DICA_BLOCK = {
		
            "type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Se estiver muito dificil você pode pedir uma dica escrevendo 'dica'"
			}
    }

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
        self.adivinhacao = jgAdivinhacao.comeca_jogo()
        self.QUESTION_BLOCK["text"]["text"] = self.QUESTION_BLOCK["text"]["text"].replace("<text>", self.adivinhacao["pergunta"])
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "blocks": [
                self.TITLE_BLOCK,
                self.DIVIDER_BLOCK,
                self.DICA_BLOCK,
                self.DIVIDER_BLOCK,
                self.QUESTION_BLOCK
            ],
        }
    
    
    def get_message_ingame(self, text, user_id):

        msg_erros = [
            "Errado <@<user_id>>! :no_mouth:",
            "Acho que não <@<user_id>> :thinking_face:",
            "Continue tentando <@<user_id>> :yum:",
            "Não é isso <@<user_id>> :neutral_face:",
            ]
        num = random.randint(0, len(msg_erros)-1)
        CORRECT_BLOCK = {	
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "<@<user_id>> ACERTOU, PARABÉNS :grinning::tada::tada::tada:"
                }
        }
        
        WRONG_BLOCK = {
            
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "<@<user_id>> Errado! :no_mouth:"
                }
        }

        CORRECT_BLOCK["text"]["text"] = CORRECT_BLOCK["text"]["text"].replace("<user_id>", user_id)


        WRONG_BLOCK["text"]["text"] = msg_erros[num]
        WRONG_BLOCK["text"]["text"] = WRONG_BLOCK["text"]["text"].replace("<user_id>", user_id)

        if text.lower() in self.adivinhacao["resposta"]:
            return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "blocks": [
                CORRECT_BLOCK
            ],
        }
        else:
            return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "blocks": [
                WRONG_BLOCK
            ],
        }

    def get_is_correct(self, text):
        if text.lower() == self.adivinhacao["resposta"]:
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
        