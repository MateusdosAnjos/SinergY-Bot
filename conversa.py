import random 

class Conversa:
    """Constructs the onboarding message and stores the state of which tasks were completed."""

    conversas = [
    "Qual seu filme favorito?",
    "Quais séries ou filmes vocês tem assistido atualmente?",
    "Três momentos marcantes da sua vida",
    "O que você faz quando está tendo um dia ruim?",
    "Quem é uma inspiração para você?",
    "Quais foram as melhores férias que já teve?",
    "Qual é o seu prato preferido? Feito por quem?",
    "Qual é o sonho mais aterrador que já teve?",
    "Conte-me uma coisa de que se orgulhe sobre si",
    "Se pudesse ser um animal, qual seria?",
    "Qual lugar do mundo você gostaria de conhecer?",
    "Qual sonho de criança você realizou?",
    "Qual seu jogo preferido?",
    "Qual seu personagem preferido dos games?",
    "Se eu pudesse ser eu seria.....",
    "Se o ano de 2020 fosse um personagem, qual seria?",
    "Conte seu momento mais feliz deste mês",
    "Qual lugar mais diferenciado que você já esteve?",
    "Filme, serie ou livros?",
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
