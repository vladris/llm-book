import asyncio
import os
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

kernel = sk.Kernel()
kernel.add_chat_service('chat_completion', OpenAIChatCompletion(
    'gpt-3.5-turbo', os.environ['OPENAI_API_KEY']))

translate_plugin = kernel.import_semantic_skill_from_directory('.', 'translate')

text = 'Aren\'t large language models amazing?'

print(asyncio.run(
    kernel.run_async(translate_plugin['to_french'], input_str=text)))
