from llm_utils import ChatTemplate

response = ChatTemplate.from_file(
    'translate.json').completion({'text': "Aren't large language models amazing?"})

print(response.choices[0].message.content)
