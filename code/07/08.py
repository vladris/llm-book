from llm_utils import ChatTemplate
import json

chat = ChatTemplate({
    'messages': [{'role': 'user', 'content': 'Your goal is to write a short 3 chapter sci-fi novella on the theme of AI ethics. Come up with 7 steps that will help you achieve the goal. Output these steps as a JSON array of large language model prompts.'}]})

plan = json.loads(chat.completion({}).choices[0].message.content)

chat = ChatTemplate({
    'messages': [{'role': 'user', 'content': 'Write a short 3 chapter sci-fi novella on the theme of AI ethics.'}]})

for step in plan:
    chat.template['messages'].append({'role': 'user', 'content': step})

    message = chat.completion({}).choices[0].message
    print(message.content)
    print('-------')
    chat.template['messages'].append({'role': message.role, 'content': message.content})

