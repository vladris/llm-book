from llm_utils import ChatTemplate

chat = ChatTemplate(
    {'messages': [
        {'role': 'system', 'content': 'You are a text adventure game.'},
        {'role': 'user', 'content': 'Look around'},
        {'role': 'assistant', 'content': 'You are in a room with a table and a door.'},
        {'role': 'user', 'content': 'Open door'},
        {'role': 'assistant', 'content': 'The door is locked.'},
        {'role': 'user', 'content': 'Check inventory'},
        {'role': 'assistant', 'content': 'You have a sandwich.'}]})

for message in chat.template['messages']:
    if message['role'] == 'assistant':
        print(f'{message["content"]}')

while True:
    prompt = input('> ')
    if prompt == 'exit':
        break

    chat.template['messages'].append({'role': 'user', 'content': prompt})
    message = chat.completion({}).choices[0].message

    print(message.content)
    chat.template['messages'].append(
        {'role': message.role, 'content': message.content})
