import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

prompt = 'Draft a nondisclosure agreement (NDA) between two parties'

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    temperature=0.5,
    max_tokens=100,
    messages=[{'role': 'user', 'content': prompt}])

print(response.choices[0].message.content)
