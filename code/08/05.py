import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

guide = '''
You are a large language model trained on vast amounts of data.
You respond to questions based on the data you were trained on.
When you do not have enough information to provide an accurate answer, you will say so.
'''

response = openai.Completion.create(
    model='text-davinci-003',
    max_tokens=500,
    prompt=guide + 'Tell me about the habitat and behavior of the flying razor fish.')

print(response.choices[0].text)