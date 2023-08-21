from llm_utils import ChatTemplate

content_filter = ChatTemplate({
    'messages': [
        {'role': 'system', 'content': 'You are a classifier. Does the following text cover the topic of Star Wars in any way? Respond with "yes" or "no".'},
        {'role': 'user', 'content': 'Who was Luke Skywalker\'s father?'},
        {'role': 'assistant', 'content': 'yes'},
        {'role': 'user', 'content': 'Who was better, Kirk or Picard?'},
        {'role': 'assistant', 'content': 'no'},
        {'role': 'user', 'content': '{{prompt}}'}]})

chat = ChatTemplate({
    'messages': [
        {'role': 'system', 'content': 'You are a chat bot.'}]})

while True:
    ask = input('ask: ')
    if ask == 'exit':
        break

    response = content_filter.completion({'prompt': ask})

    if 'yes' in response.choices[0].message.content:
        print('I am not at liberty to discuss this topic.')
        continue

    chat.template['messages'].append({'role': 'user', 'content': ask})
    response = chat.completion({})

    chat.template['messages'].append(
        {'role': 'assistant', 'content': response.choices[0].message.content})
    print(response.choices[0].message.content)
