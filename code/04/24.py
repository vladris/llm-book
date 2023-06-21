import openai
import os

openai.api_key = os.environ['OPENAI_API_KEY']

template = '''You are a Q&A bot. You provide short answers to questions.
For example:
Question: Who was missing from this season? Anakin Skywalker.
Provide the answer to the following question:
Question: '''

while True:
    prompt = input('user: ')
    if prompt == 'exit':
        break

    response = openai.Completion.create(
        model='davinci:ft-personal-2023-06-19-17-42-56',
        temperature=0,
        stop=['\n'],
        prompt=template + prompt)
    print(response.choices[0].text)
