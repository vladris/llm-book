from llm_utils import Template

chat = Template({
    'max_tokens': 500,
    'prompt': 'Tell me about the habitat and behavior of the flying razor fish.'})

print(chat.completion({}).choices[0].text)
