from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
    ('system', 'You are an English to French translator.'),
    ('user', 'Translate this to French: {text}')
])

llm = ChatOpenAI()

response = llm(template.format_messages(
    text='Aren\'t large language models amazing?'))

print(response)
