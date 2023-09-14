import asyncio
import os
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion, OpenAITextEmbedding

kernel = sk.Kernel()
kernel.add_chat_service('chat_completion', OpenAIChatCompletion(
    'gpt-3.5-turbo', os.environ['OPENAI_API_KEY']))

qa_plugin = kernel.import_semantic_skill_from_directory('.', 'qa')

kernel.add_text_embedding_generation_service('ada', OpenAITextEmbedding(
    'text-embedding-ada-002', os.environ['OPENAI_API_KEY']))

kernel.register_memory_store(memory_store=sk.memory.VolatileMemoryStore())

for f in os.listdir('../racing'):
    path = os.path.join('../racing', f)
    with open(path, 'r') as f:
        text = f.read()
        asyncio.run(kernel.memory.save_information_async(
            collection='racing',
            text=text,
            id=path))

while True:
    prompt = input('user: ')
    if prompt == 'exit':
        break

    data = asyncio.run(kernel.memory.search_async('racing', prompt, limit=1))

    context = kernel.create_new_context()
    context["data"] = data[0].text
    context["prompt"] = prompt

    print(asyncio.run(kernel.run_async(qa_plugin['qa'], input_vars=context.variables)))
