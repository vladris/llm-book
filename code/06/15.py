import chromadb
from chromadb.utils import embedding_functions
from chromadb.config import Settings
import json
from llm_utils import ChatTemplate
import os

client = chromadb.Client(Settings(
    chroma_db_impl='duckdb+parquet',
    persist_directory='functions'))

collection = client.get_collection(
    'functions',
    embedding_function=embedding_functions.OpenAIEmbeddingFunction(
        api_key=os.environ['OPENAI_API_KEY'],
        model_name="text-embedding-ada-002"
    ))

chat = ChatTemplate(
    {'temperature': 0,
     'messages': [{'role': 'system', 'content': 'You are an AI personal assistant'}],
     'functions': []})

while True:
    prompt = input('user: ')
    if prompt == 'exit':
        break

    chat.template['messages'].append({'role': 'user', 'content': prompt})

    functions = collection.query(
        query_texts=[prompt], n_results=2)['documents']
    chat.template['functions'] = [json.loads(doc) for doc in functions[0]]

    print(chat.template)

    # ...
