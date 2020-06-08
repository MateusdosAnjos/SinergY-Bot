import random 

perguntas = [
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

respostas = [
  "batman",
  "antártida",
  "sapato",
  "cebola",
  "porta",
  "respira",
  "barco à vela",
  "tempo",
  "ovo",
]

dicas = [
  "Ele teme o Ozzy Osbourne",
  "Nem todo deserto é quente.",
  "Quem anda são os pés",
  "Pense em alimentos",
  "Dizemos que quando uma se fecha outras se abrem",
  "Uma ordem para fazer algo que fazemos sempre",
  "Qual outra coisa feita de cera que tem no barco? Talvez não seja exatamente a mesma coisa....",
  "Oh Ok.... time's up!",
  "Égsses.... Égsses preciooous...",
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
