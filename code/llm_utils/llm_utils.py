import copy
import json
import openai
import os
import re
import tiktoken

openai.api_key = os.environ['OPENAI_API_KEY']
if openai.api_key is None:
    raise Exception('OPENAI_API_KEY not set')


def insert_params(string, **kwargs):
    pattern = r"{{(.*?)}}"
    matches = re.findall(pattern, string)
    for match in matches:
        replacement = kwargs.get(match.strip())
        if replacement is not None:
            string = string.replace("{{" + match + "}}", replacement)
    return string


class Template:
    def __init__(self, template):
        self.template = template

    def from_file(template_file):
        with open(template_file, 'r') as f:
            template = json.load(f)

        return Template(template)

    def completion(self, parameters):
        instance = copy.deepcopy(self.template)
        instance['prompt'] = insert_params(instance['prompt'], **parameters)

        return openai.Completion.create(
            model='text-davinci-003',
            **instance)


class ChatTemplate:
    def __init__(self, template):
        self.template = template

    def from_file(template_file):
        with open(template_file, 'r') as f:
            template = json.load(f)

        return ChatTemplate(template)

    def completion(self, parameters):
        instance = copy.deepcopy(self.template)
        for item in instance['messages']:
            item['content'] = insert_params(item['content'], **parameters)

        return openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            **instance)


def count_tokens(messages):
    # Note this encoding might change in future versions of gpt-3.5-turbo
    encoding = tiktoken.get_encoding('cl100k_base')

    # Every message follows <|start|>{role/name}\n{content}<|end|>\n
    tokens_per_message = 4
    # If there's a name, the role is omitted
    tokens_per_name = -1

    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    # Every reply is primed with <|start|>assistant<|message|>
    num_tokens += 3
    return num_tokens


def get_embedding(text):
    return openai.Embedding.create(
        input=[text.replace('\n', ' ')],
        model='text-embedding-ada-002')['data'][0]['embedding']


def cosine_distance(a, b):
    return 1 - sum([a_i * b_i for a_i, b_i in zip(a, b)]) / (sum([a_i ** 2 for a_i in a]) ** 0.5 * sum([b_i ** 2 for b_i in b]) ** 0.5)
