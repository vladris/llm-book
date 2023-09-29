import copy
import json
import openai
import os
import re

openai.api_key = os.environ['OPENAI_API_KEY']

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
        instance['prompt'] = format(instance['prompt'], **parameters)

        return openai.Completion.create(
            model='gpt-3.5-turbo-instruct',
            **instance)
