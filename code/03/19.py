from llm_utils import ChatTemplate

response = ChatTemplate.from_file('writer_chat.json').completion(
    {'action': 'compose',
     'document': 'a haiku about large language models'})

print(response.choices[0].message.content)
