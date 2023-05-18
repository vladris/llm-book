from llm_utils import ChatTemplate
import re

def step(template_file, pattern):
    chat_template = ChatTemplate.from_file(template_file)
    print(chat_template.template['messages'][-1]['content'])
    while True:
        prompt = input('Customer: ')
        chat_template.template['messages'].append({'role': 'user', 'content': prompt})

        message = chat_template.completion({}).choices[0].message
        if 'DONE' in message.content:
            return re.search(pattern, message.content, re.DOTALL).group(1).strip() 

        print(f'{message.content}')
        chat_template.template['messages'].append({'role': message.role, 'content': message.content})


order = step('order.json', r'ORDER(.*)DONE')
phone = step('phone.json', r'PHONE(.*)DONE')

print()
print(order)
print(phone)