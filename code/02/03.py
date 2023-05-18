import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')
response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role': 'user', 'content': 'Say "Hello world" in Python'}
    ])

print(response.choices[0].message)
