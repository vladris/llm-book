import copy
import json
import openai
import os

openai.api_key = os.environ['OPENAI_API_KEY']

class Template:
    def __init__(self, template):
        self.template = template

    def from_file(template_file):
        with open(template_file, 'r') as f:
            template = json.load(f)

        return Template(template)

    def completion(self, parameters):
        instance = copy.deepcopy(self.template)
        instance['prompt'] = instance['prompt'].format(**parameters)

        return openai.Completion.create(
            model='text-davinci-003',
            **instance)
