# KOD WZIĘTY Z: https://github.com/ollama/ollama/blob/main/examples/python-simplechat/client.py
# Zmodyfikowany przez: Emilia Wiśniewska

import json
import requests # powinnno działać, jeśli nie to: pip install requests

# NOTE: żeby działało musi być uruchomiona ollama ("$ ollama serve" lub uruchomiona aplikacja)
model = "llama2"


def answer(messages):
    r = requests.post(
        "http://0.0.0.0:11434/api/chat",
        json={"model": model, "messages": messages, "stream": False},
    )
    r.raise_for_status()
 
    body = json.loads(r.text)
    message = body.get("message", "")
    content = message.get("content", "")
    return content


while True:
    user_input = input("Enter a prompt: ")
    if not user_input:
        exit()
    print("llama2:", answer([{"role": "user", "content": user_input}]))
    # print("\n")
