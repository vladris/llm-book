from llm_utils import ChatTemplate

chat = ChatTemplate(
    {'messages': [{'role': 'system', 'content': 'You are an AI chat program.'}]})

while True:
    prompt = input('user: ')
    if prompt == 'exit':
        break

    chat.template['messages'].append({'role': 'user', 'content': prompt})
    message = chat.completion({}).choices[0].message

    print(f'{message.role}: {message.content}')
    chat.template['messages'].append(
        {'role': message.role, 'content': message.content})
