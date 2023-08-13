from llm_utils import ChatTemplate

chat = ChatTemplate({
    'messages': [{'role': 'user', 'content': 'Tell me 5 facts about ostriches, provide references.'}]})

print(chat.completion({}).choices[0].message.content)
