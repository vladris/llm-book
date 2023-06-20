from llm_utils import ChatTemplate

response = ChatTemplate.from_file(
    'xml.json').completion({'entity': 'Elon Musk'})

print(response.choices[0].message.content)
