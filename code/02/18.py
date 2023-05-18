import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

prompt = 'Generate a name for a new coffee brand.'

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    n=3,
    messages=[{'role': 'user', 'content': prompt}])

for choice in response.choices:
    print(choice.message.content)
