import json
from llm_utils import ChatTemplate


def get_emails(names):
    print(f'* Getting emails for {names}')

    address_book = {
        'John Doe': 'john.doe@example.com',
        'Jane Doe': 'jane.doe@example.com',
    }
    emails = {}

    for name in names:
        emails[name] = address_book[name]

    return emails


def schedule_meeting(subject, recipients, time):
    print(f"* Meeting '{subject}' scheduled for {time} with {recipients}")
    return {'success': True}


def process_function_call(function_call):
    name = function_call.name
    args = json.loads(function_call.arguments)

    functions = {
        'get_emails': get_emails,
        'schedule_meeting': schedule_meeting,
    }

    return functions[name](**args)


chat = ChatTemplate.from_file('personal_assistant.json')

while True:
    prompt = input('> ')
    if prompt == 'exit':
        break

    chat.template['messages'].append({'role': 'user', 'content': prompt})

    while True:
        message = chat.completion({}).choices[0].message

        if 'function_call' in message:
            result = process_function_call(message.function_call)
            chat.template['messages'].append(
                {'role': 'function', 'name': message.function_call.name, 'content': json.dumps(result)})
        else:
            break

    print(message.content)
    chat.template['messages'].append(
        {'role': message.role, 'content': message.content})
