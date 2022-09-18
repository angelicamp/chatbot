from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('Aurora')
chatbot.storage.drop()
conversa = [
    "bom dia",
    "Bom dia !"
    "Tudo bem com vc?",
    "tudo bem e voce?",
    "tudo bem",
    "Como posso te ajudar?"
    "Tudo bem também! Como posso te ajudar?",
    "Como posso te ajudar?",
    "fazendo um pix",
    "Xiiii... a vida nao ta facil pra ninguem!",
    "marcar uma consulta",
    "Voce pode marcar uma consulta direto com o seu plano",
    "faz café pra mim?",
    "Nao sou sua empregada",
    "que horas são?",
    "Hora de voce comprar um relogio",
    "estou triste",
    "Come chocolate que passa...",
    "gostei da ideia",
    "Eu sei, so tenho ideias incriveis"
]
trainer = ListTrainer(chatbot)
trainer.train(conversa)
while True:
    resposta = chatbot.get_response(input())
    print(resposta)
