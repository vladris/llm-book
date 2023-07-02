import json


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
