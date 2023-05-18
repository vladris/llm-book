import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

prompt = 'Write a short story about a man who discovers a mysterious book in an old library.'

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    temperature=1.5,
    max_tokens=100,
    messages=[{'role': 'user', 'content': prompt}])

print(response.choices[0].message.content)
