from llm_utils import ChatTemplate, get_embedding, cosine_distance
import json

embeddings = json.load(open('embeddings.json', 'r'))


def nearest_embedding(embedding):
    nearest, nearest_distance = None, 1

    for path, embedding2 in embeddings.items():
        distance = cosine_distance(embedding, embedding2)
        if distance < nearest_distance:
            nearest, nearest_distance = path, distance

    return nearest


def context_url(context):
    return f'https://raw.githubusercontent.com/vladris/llm-book/main/code/{context[3:]}'


chat = ChatTemplate(
    {'messages': [{'role': 'system', 'content': 'You are a Q&A AI. Your responses always include a link to the source of the information you provide.'},
                  {'role': 'system', 'content': 'Here are some facts that can help you answer the following question: {{data}}. The orginal URL for these facts is {{url}}.'},
                  {'role': 'user', 'content': '{{prompt}}'}]})


while True:
    prompt = input('user: ')
    if prompt == 'exit':
        break

    context = nearest_embedding(get_embedding(prompt))
    data = open(context, 'r').read()
    url = context_url(context)

    message = chat.completion(
        {'data': data, 'url': url, 'prompt': prompt}).choices[0].message

    print(f'{message.role}: {message.content}')
