# pip install openai
# MAC/LINUX: export OPENAI_API_KEY=...
# WINDOWS: setx OPENAI_API_KEY "..."

from . import secrets
from openai import OpenAI

client = OpenAI(
    api_key=secrets.OPENAI_API_KEY
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  messages=[
    {"role": "system", "content": "QA Chatbot that helps with testing questions."},
    {"role": "user", "content": "How should I validate html inputs?"},
    {"role": "assistant", "content": "You can use the HTML5 form validation feature to validate the input fields."}    
  ],
  # 0-2
  temperature=0.2
)

print(completion.choices[0].message)

