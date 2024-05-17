# KOD NA PODSAWIE: https://github.com/ollama/ollama/blob/main/examples/python-simplechat/client.py
# Zmodyfikowany przez: Emilia Wiśniewska

import json
import requests # powinnno działać, jeśli nie to: pip install requests
import click

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


def post_question(user_input):
    question = [{"role": "user", "content": user_input}]
    return answer(question)


"""
mozliwosc odpalenia wielokrotnego:
"""
@click.command()
@click.option('--count', default=1, help='Number of sent "hi"s to llama2')
def llama_sample_main(count):
    # while True:
    #     user_input = input("\033[1;92m>>> \033[0;37m")
    #     if not user_input:
    #         exit()
    #     print("\033[1;92mllama2:\033[0;37m", post_question(user_input))
    #     print("\n")
    for i in range(count):
        print(post_question("hi"));


if __name__ == "__main__":
    llama_sample_main()

