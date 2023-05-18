import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

prompt = 'Write a story about a young girl who discovers a magical world.'
stop = ['The end', 'To be continued', 'And they lived happily ever after.']

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[{'role': 'user', 'content': prompt}],
    stop=stop,
    stream=True,
    max_tokens=500)

for chunk in response:
    if hasattr(chunk.choices[0].delta, 'content'):
        print(chunk.choices[0].delta.content, end='', flush=True)
