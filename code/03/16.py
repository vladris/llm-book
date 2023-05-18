import copy
import json
import openai
import os

openai.api_key = os.environ['OPENAI_API_KEY']

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
            item['content'] = item['content'].format(**parameters)

        return openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            **instance)
