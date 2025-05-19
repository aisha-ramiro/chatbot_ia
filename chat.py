import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import tkinter as tk
from tkinter import scrolledtext

load_dotenv(dotenv_path='API.env')
api_key = os.getenv("API_KEY")

cliente = genai.Client(api_key=api_key)

modelo ="gemini-2.0-flash" 

chat_config = types.GenerateContentConfig(
    system_instruction= "Você é um chatbot e sempre responde de maneira sucinta.",
)

chat = cliente.chats.create(model=modelo, config=chat_config)
chat.get_history()

def enviar_prompt():
    prompt = entrada.get()
    if prompt.lower() == "sair":
        janela.destroy()
        return
    if prompt.strip() == "":
        return
    entrada.delete(0, tk.END)
    resposta = chat.send_message(prompt)
    historico.insert(tk.END, f"Você: {prompt}\n", "user")
    historico.insert(tk.END, f"Bot: {resposta.text}\n\n", "bot")
    historico.see(tk.END)


janela = tk.Tk()
janela.title("Chatbot Gemini")


historico = scrolledtext.ScrolledText(janela, wrap=tk.WORD, height=20, width=60)
historico.tag_config("user", foreground="blue")
historico.tag_config("bot", foreground="green")
historico.pack(padx=10, pady=10)


entrada = tk.Entry(janela, width=50)
entrada.pack(side=tk.LEFT, padx=10, pady=10)
entrada.focus()


botao_enviar = tk.Button(janela, text="Enviar", command=enviar_prompt)
botao_enviar.pack(side=tk.LEFT, padx=5)


janela.bind('<Return>', lambda event: enviar_prompt())

janela.mainloop()


