# pip install openai
# MAC/LINUX: export OPENAI_API_KEY=...
# WINDOWS: setx OPENAI_API_KEY "..."

from openai import OpenAI
client = OpenAI(
    api_key="sk-proj-EnFQ80pADZV6pc1PQOVuT3BlbkFJ4GKZJatjtmZd00yFqYYo"
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

