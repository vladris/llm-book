from llm_utils import ChatTemplate

with open('books.txt', 'r') as f:
    content = f.read().split('\n\n')

books = {}
for book in content:
    title, description = book.split('\n---\n')
    books[title] = description.strip()

chat = ChatTemplate(
    {'messages': [{'role': 'system', 'content': 'You are an AI chat program.'}]})

while True:
    prompt = input('user: ')
    if prompt == 'exit':
        break

    for book in books:
        if book in prompt:
            chat.template['messages'].append({'role': 'user', 'content':
                                              'Here is a description of ' + book + ': ' + books[book] + '.'})

    chat.template['messages'].append({'role': 'user', 'content': prompt})
    message = chat.completion({}).choices[0].message

    print(f'{message.role}: {message.content}')
    chat.template['messages'].append(
        {'role': message.role, 'content': message.content})
