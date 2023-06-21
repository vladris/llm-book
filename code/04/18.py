from llm_utils import ChatTemplate
import os

template = ChatTemplate.from_file('jsonl.json')
jsonl = ''

for f in os.listdir('../racing'):
    with open(os.path.join('../racing', f), 'r') as f:
        text = f.read()

    response = template.completion({'info': text, 'n': '20'})
    jsonl += response.choices[0].message.content.strip() + '\n'

with open('racing.jsonl', 'w+') as f:
    f.write(jsonl)
