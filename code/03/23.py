from llm_utils import ChatTemplate
import json

selection = ChatTemplate.from_file('selection_chat.json')

while True:
    ask = input('ask: ')
    if ask == 'exit':
        break

    response = selection.completion({'ask': ask})
    print(response.choices[0].message.content)
    selected = json.loads(response.choices[0].message.content)

    response = ChatTemplate.from_file(selected['as'] + '_chat.json').completion({
        'action': selected['action'],
        'document': selected['document']})
    print(response.choices[0].message.content)
