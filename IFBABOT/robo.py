import time
from chatterbot import ChatBot

CONFIANCA_MINIMA = 0.70 # = a 70%

def configurar():
    
    time.clock = time.time
    robo = ChatBot("Robô de atendimento do IFBA", 
                   read_only = True, 
                   logic_adapters = [{"import_path": "chatterbot.logic.BestMatch"}]
                   )

    return True, robo

def executar(robo):
    while True:
        mensagem = input("\nDigite alguma coisa: ")
        resposta = robo.get_response(mensagem.lower())

        if resposta.confidence >= CONFIANCA_MINIMA:
            print(f"IFBA >> {resposta.text} \nConfiança = {resposta.confidence}")
        else:
            print("Infelizmente eu não sei responder essa pergunta 😔")
            print(f"Confiança = {resposta.confidence}")
            print("Pergunte outra coisa: ")

if __name__ == "__main__":
    configurado, robo = configurar()

    if configurado:
       executar(robo)