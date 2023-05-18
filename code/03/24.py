from llm_utils import ChatTemplate

chat = ChatTemplate(
    {'messages': [{'role': 'system', 'content': 'You are an AI chat program.'},
                  {'role': 'user', 'content': None}]})

while True:
    prompt = input('user: ')
    if prompt == 'exit':
        break

    chat.template['messages'][1]['content'] = prompt
    message = chat.completion({'prompt': prompt}).choices[0].message

    print(f'{message.role}: {message.content}')
