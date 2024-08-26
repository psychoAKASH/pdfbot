import os
from email.policy import default

from openai import OpenAI
import helpers

OPENAI_API_KEY = helpers.config("OPENAI_API_KEY",default=None)
def get_openai_client():
    return OpenAI(api_key=OPENAI_API_KEY,)

def chat_with_openai(message,model="gpt-3.5-turbo",raw = False):
    client = get_openai_client()

    response =  client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are an amazing code assistant",
            },
            {
                "role": "user",
                "content": message,
            }
        ],
        model=model,
)
    if raw:
        return response
    return response.choices[0].message.content