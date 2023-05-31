import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

chat_messages = [] 

while True:
  user_message = input("You: ")
  chat_messages.append({"role": "user", "content": user_message})

  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=chat_messages,
    temperature=0,
    # max_tokens=100
  )

  ai_response = response.choices[0].message.content
  chat_messages.append({"role": "assistant", "content": ai_response})
  print("AI: ", ai_response)
