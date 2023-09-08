import asyncio
import os
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel.semantic_functions.prompt_template_config import PromptTemplateConfig

kernel = sk.Kernel()
kernel.add_chat_service('chat_completion', OpenAIChatCompletion(
    'gpt-3.5-turbo', os.environ['OPENAI_API_KEY']))

prompt_config = PromptTemplateConfig(
    completion=PromptTemplateConfig.CompletionConfig(
        chat_system_prompt='You are an English to French translator.'
    )
)

prompt_template = sk.ChatPromptTemplate(
    'Translate this to French: {{$input}}',
    kernel.prompt_template_engine,
    prompt_config)

function_config = sk.SemanticFunctionConfig(prompt_config, prompt_template)

translate = kernel.register_semantic_function(
    None, 'translate', function_config)

text = 'Aren\'t large language models amazing?'

print(asyncio.run(kernel.run_async(translate, input_str=text)))
