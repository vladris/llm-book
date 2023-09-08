import os
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

kernel = sk.Kernel()
kernel.add_chat_service('chat_completion', OpenAIChatCompletion(
    'gpt-3.5-turbo', os.environ['OPENAI_API_KEY']))

prompt = 'Say "Hello world" in Python.'

hello_world = kernel.create_semantic_function(prompt)

print(hello_world())
