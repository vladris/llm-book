import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')
history = []

while True:
    prompt = input('user: ')
    if prompt == 'exit':
        break

    history.append({'role': 'user', 'content': prompt})
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=history)

    message = response.choices[0].message

    print(f'{message.role}: {message.content}')
    history.append({'role': message.role, 'content': message.content})
