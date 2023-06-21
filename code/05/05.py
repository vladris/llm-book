from llm_utils import ChatTemplate, count_tokens

chat = ChatTemplate(
    {'messages': [{'role': 'system', 'content': 'You are an AI chat program.'}]})

TOKEN_LIMIT = 1000

while True:
    prompt = input('user: ')
    if prompt == 'exit':
        break

    chat.template['messages'].append({'role': 'user', 'content': prompt})
    while count_tokens(chat.template['messages']) > TOKEN_LIMIT:
        chat.template['messages'].pop(0)

    message = chat.completion({}).choices[0].message

    print(f'{message.role}: {message.content}')
    chat.template['messages'].append(
        {'role': message.role, 'content': message.content})
