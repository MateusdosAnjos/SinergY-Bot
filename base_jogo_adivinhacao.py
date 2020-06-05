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
    num = randint(1,len(perguntas))
    pergunta = select_adinhacao()
    resposta = get_resposta()
    dica = get_dica

    return {
        "pergunta" : pergunta,
        "resposta" : resposta,
        "dica" : dica
    }

def select_adinhacao(num : int):
    return pergunta[num]

def get_dica(id : int):
    return dicas[id]

def get_resposta(id : int):
    return respostas[id]
