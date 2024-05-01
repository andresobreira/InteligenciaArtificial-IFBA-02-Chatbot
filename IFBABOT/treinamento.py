from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time
import json

CAMINHO = "D:\\Dev\\IFBA\\IA_02_Chatbot\\IFBABOT\\conversas\\"
CONVERSAS = [
    CAMINHO+"saudacoes.json",
    CAMINHO+"informacoes_basicas.json",
    CAMINHO+"sistemas_de_informacao.json"
]

# 1. Devolve um treinador de robô.
def configurar():
    time.clock = time.time
    robo = ChatBot("Robô de atendimento do IFBA")
    treinador = ListTrainer(robo)

    return True, treinador

# 2. Carrega as conversas a partir dos jsons
def carregar_conversas():
    carregadas, conversas = True, []

    for arquivo_de_conversas in CONVERSAS:
        try:
            with open(arquivo_de_conversas, "r", encoding="utf8" ) as arquivo:
                para_treinar = json.load(arquivo)
                conversas.append(para_treinar["conversas"])

                arquivo.close()
        
        except Exception as e:
            carregadas = False
            print(str(e))

    return carregadas, conversas

# 3. Usa o treinador para treinar o robô com as conversas
def treinar(treinador, conversas):
    for conversa in conversas:
        for mensangens_resposta in conversa:
            mensagens = mensangens_resposta["mensagens"]
            resposta = mensangens_resposta["resposta"]

            print(f"Treinando o robô. Mensagens: {mensagens}, resposta: {resposta}")
            for mensagem in mensagens:
                treinador.train([mensagem,resposta])


if __name__ == "__main__":
    configurado, treinador = configurar()

    if configurado:
        carregadas, conversas = carregar_conversas()

        if carregadas:
            treinar(treinador, conversas)
        