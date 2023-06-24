import chromadb
from chromadb.utils import embedding_functions
from chromadb.config import Settings
from llm_utils import ChatTemplate
import os

client = chromadb.Client(Settings(
    chroma_db_impl='duckdb+parquet',
    persist_directory='racing'))

collection = client.get_collection(
    'pod-racing',
    embedding_function=embedding_functions.OpenAIEmbeddingFunction(
        api_key=os.environ['OPENAI_API_KEY'],
        model_name="text-embedding-ada-002"
    ))

chat = ChatTemplate(
    {'messages': [{'role': 'system', 'content': 'You are a Q&A AI.'},
                  {'role': 'system', 'content': 'Here are some facts that can help you answer the following question: {{data}}'},
                  {'role': 'user', 'content': '{{prompt}}'}]})

while True:
    prompt = input('user: ')
    if prompt == 'exit':
        break

    data = collection.query(query_texts=[prompt], n_results=1)[
        'documents'][0][0]

    message = chat.completion(
        {'data': data, 'prompt': prompt}).choices[0].message

    print(f'{message.role}: {message.content}')
