from llm_utils import ChatTemplate

chat = ChatTemplate({
    'messages': [{'role': 'user', 'content': 'Output the Python code for counting how many times the letter "e" show up in the days of the week.'}]})

print(chat.completion({}).choices[0].message.content)
