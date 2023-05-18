from llm_utils import ChatTemplate
import json

selection = ChatTemplate.from_file('selection_chat.json')

while True:
    ask = input('ask: ')
    if ask == 'exit':
        break

    response = selection.completion({'ask': ask})
    print(response.choices[0].message.content)
    selection = json.loads(response.choices[0].message.content)

    response = ChatTemplate(selection['as'] + '_chat.json').completion({
        'action': selection['action'],
        'document': selection['document']})
    print(response.choices[0].message.content)
