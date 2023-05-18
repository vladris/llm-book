from llm_utils import ChatTemplate

selection = ChatTemplate.from_file('selection_chat.json')

response = selection.completion(
    {'ask': 'I need an open-source license document'})

print(response.choices[0].message.content)

response = selection.completion(
    {'ask': 'I need a funny skit'})

print(response.choices[0].message.content)
