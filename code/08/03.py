import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

response = openai.Completion.create(
    model='text-davinci-003',
    max_tokens=500,
    prompt='Tell me about the habitat and behavior of the flying razor fish.')

print(response.choices[0].text)
