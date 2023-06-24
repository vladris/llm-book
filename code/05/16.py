import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
import os

client = chromadb.Client(Settings(
    chroma_db_impl='duckdb+parquet',
    persist_directory='racingdb'))

collection = client.create_collection(
    'pod-racing',
    embedding_function=embedding_functions.OpenAIEmbeddingFunction(
        api_key=os.environ['OPENAI_API_KEY'],
        model_name="text-embedding-ada-002"
    ))

for f in os.listdir('../racing'):
    path = os.path.join('../racing', f)
    with open(path, 'r') as f:
        text = f.read()

    text = text.replace('\n', ' ')

    collection.add(documents=[text], ids=[path])

client.persist()
