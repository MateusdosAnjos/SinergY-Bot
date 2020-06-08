class Conversa:
    """Constructs the onboarding message and stores the state of which tasks were completed."""
    import random 

    conversas = [
    "Qual super-heroi é conhecido como 'o cavaleiro das trevas'?",
    "Qual o maior deserto da Terra?",
    "O que é feito para andar mas não anda?",
    "Você tira a minha pele e eu não choro, mas você sim. O que sou?",
    "O que é que vai e vem sem sair do lugar?",
    "O que a uva verde falou para a uva roxa?",
    "Qual é o barco feito de cera?",
    "Essa é a coisa que a tudo devora. Feras, aves, plantas, flora. Aço e ferro são sua comida, e a dura pedra por ele moída; Aos reis abate, à cidade arruína, E a alta montanha faz pequenina.",
    "Caixinha sem gonzos,tampa ou cadeado, Lá dentro escondido um tesouro dourado",
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
        num = random.randint(0, len(conversas)-1)
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
