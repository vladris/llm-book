from llm_utils import ChatTemplate

chat = ChatTemplate({
    'messages': [{'role': 'user', 'content': 'How many times does the letter "e" show up in the days of the week? Think step by step.'}]})

print(chat.completion({}).choices[0].message.content)
