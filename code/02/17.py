import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

prompt = 'Write an article about the history of space exploration.'

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    max_tokens=1000,
    messages=[{'role': 'user', 'content': prompt}])

print(response.choices[0].message.content)
