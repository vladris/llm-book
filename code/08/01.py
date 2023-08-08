from llm_utils import ChatTemplate

chat = ChatTemplate({
    'messages': [{'role': 'user', 'content': 'Tell me about the habitat and behavior of the flying razor fish.'}]})

print(chat.completion({}).choices[0].message.content)
