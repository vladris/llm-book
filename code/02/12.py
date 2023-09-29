import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')
response = openai.Completion.create(
    model='gpt-3.5-turbo-instruct',
    prompt='Say "Hello world" in Python')

print(response)
