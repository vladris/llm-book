# Appendix A: LLM Utilities

Throughout the book, we’ve been relying on a few helper functions imported from
llm_utils. This is a small module available as part of the code supporting this
book. You can find it on GitHub, at <https://github.com/vladris/llm-book>, under
`/code/llm_utils` folder. In fact, we looked at all the components of this
module throughout the book.

For completeness, here is the full code of `llm_utils.py`:

```python
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
            model='gpt-3.5-turbo-instruct',
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
```

The module sets the `OPENAI_API_KEY` or, in case one is not present, raises an
exception. The provided utilities are:

* The `Template` class, a completion template. This can be created from an
  object or loaded from a file conforming to the OpenAI API schema. The
  `completion()` function instantiates the template with actual parameters and
  sends a request to `gpt-3.5-turbo-instruct`.
* The `ChatTemplate` class is similar to `Template`, but represents a chat
  completion template and sends the request to `gpt-3.5-turbo`.
* The `count_tokens()` function uses the `tiktoken` library and provides a token
  count for a list of messages in a chat completion.
* The `get_embedding()` function just wraps a call to create an embedding given
  some text, using `text-embedding-ada-002` model.
* The `cosine_distance()` function is an implementation of the formula to
  compute cosine distance.

As mentioned earlier, we already each of these when we discussed the
corresponding topics. The module just brings them together and makes them
available to other code as needed.
