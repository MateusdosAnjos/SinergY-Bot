import random 

perguntas = [
  "Qual super-heroi é conhecido como 'o cavaleiro das trevas'?",
  "Qual o maior deserto da Terra?",
  "Em que ano foi escrita a atual Constituição Brasileira?"
]

respostas = [
  "Batman",
  "Antártida",
  "1988"
]

dicas = [
  "A",
  "Lá é muito frio",
  "C"
]

def comeca_jogo():
    num = random.randint(0, len(perguntas)-1)
    pergunta = select_adivinhacao(num)
    resposta = get_resposta(num)
    dica = get_dica(num)

    return {
        "pergunta" : pergunta,
        "resposta" : resposta,
        "dica" : dica
    }

def select_adivinhacao(num : int):
    return perguntas[num]

def get_dica(id : int):
    return dicas[id]

def get_resposta(id : int):
    return respostas[id]
