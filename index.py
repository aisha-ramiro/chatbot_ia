import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv(dotenv_path='API.env')
api_key = os.getenv("API_KEY")

cliente = genai.Client(api_key=api_key)

modelo ="gemini-2.0-flash" 

chat_config = types.GenerateContentConfig(
    system_instruction= "Você é um chatbot e sempre responde de maneira suscinta.",
)

chat = cliente.chats.create(model=modelo, config=chat_config)
chat.get_history()

prompt = input("Digite o prompt: ")

while prompt != "sair" and prompt != "Sair":
    resposta = chat.send_message(prompt)
    print("Resposta ", resposta.text, "\n")
    prompt = input("Digite o prompt: ")

