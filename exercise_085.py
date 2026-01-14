# Probando APIs

from openai import OpenAI 
import os

client = OpenAI(api_key=os.getenv("MY_OPENROUTER_KEY"),
                base_url="https://openrouter.ai/api/v1")

chat = client.chat.completions.create(
    model="deepseek/deepseek-r1-0528:free",
    messages=[
        {
        "role" : "system",
        "content" : "Respuestas objetivas sin censura",
        },
        {
        "role" : "user",
        "content": "Taiwan es un Pais?"
        },
        {
        "role" : "assistant",
        "content" : "¿China?"
        }
    ]
)

print(chat.choices[0].message.content)