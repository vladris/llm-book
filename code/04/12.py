from llm_utils import ChatTemplate

chat = ChatTemplate.from_file('sentiment.json')

while True:
    prompt = input('> ')
    if prompt == 'exit':
        break

    message = chat.completion({'review': prompt}).choices[0].message

    print(message.content)
