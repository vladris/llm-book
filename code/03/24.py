from llm_utils import ChatTemplate

chat = ChatTemplate(
    {'messages': [{'role': 'system', 'content': 'You are an AI chat program.'},
                  {'role': 'user', 'content': '{{prompt}}'}]})

while True:
    prompt = input('user: ')
    if prompt == 'exit':
        break

    message = chat.completion({'prompt': prompt}).choices[0].message

    print(f'{message.role}: {message.content}')
