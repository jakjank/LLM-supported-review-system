# KOD WZIĘTY Z: https://github.com/ollama/ollama/blob/main/examples/python-simplechat/client.py
# Zmodyfikowany przez: Emilia Wiśniewska

# jeszcze nie wiem, czy dziala bo mi na windowsie nie chce dzialac

import json
import requests # powinnno działać, jeśli nie to: pip install requests

# NOTE: ollama must be running for this to work, start the ollama app or run `ollama serve`
model = "llama2"  # TODO: update this for whatever model you wish to use


def chat(messages):
    r = requests.post(
        "http://0.0.0.0:11434/api/chat",
        json={"model": model, "messages": messages, "stream": False},
    )
    r.raise_for_status()
 
    body = json.loads(r.text)
    message = body.get("message", "")
    content = message.get("content", "")
    # output = content
    print(content)
    return message

def main():
    messages = []

    while True:
        user_input = input("Enter a prompt: ")
        if not user_input:
            exit()
        print()
        messages.append({"role": "user", "content": user_input})
        message = chat(messages)
        messages.append(message)
        print("\n\n")
