import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

prompt = 'Write a paragraph about the benefits of meditation.'
suffix = 'Meditation has been shown to reduce stress and anxiety, improve focus and attention, and promote overall well-being.'

response = openai.Completion.create(
    model='text-davinci-003',
    prompt=prompt,
    suffix=suffix,
    max_tokens=100)

print(response.choices[0].text)
