import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

prompt = 'What are the main causes of climate change?'

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    max_tokens=50,
    messages=[{'role': 'user', 'content': prompt}])

print(response.choices[0].message.content)
