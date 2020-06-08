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
  "Quais são as partículas que não gostam de estudar?",
  "O que é que começa na mata, vai a ponta da nuvem e termina no jardim?",
  "O que é varinha de condão e ao tocar numa caixinha faz luz na escuridão?",
  "O que nasce uma vez, nasce duas vezes, mas na terceira não nasce mais?",
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
  "partículas de antimatéria",
  "letra m",
  "palito de fósforo",
  "dente",
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
  "talvez 'matéria' esteja envolvida",
  "existe uma vantagem em ler a charada. Seria mas difícil ouvi-la",
  "o fogo pode iluminar a escuridão...",
  "Da primeira vez é sempre de leite",
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
