from llm_utils import ChatTemplate

response = ChatTemplate.from_file('lawyer_chat.json').completion(
    {'action': 'draft',
     'document': 'a nondisclosure agreement (NDA) between two parties'})

print(response.choices[0].message.content)
