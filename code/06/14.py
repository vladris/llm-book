import chromadb
from chromadb.config import Settings
import json
from llm_utils import get_embedding
import os

client = chromadb.Client(Settings(
    chroma_db_impl='duckdb+parquet',
    persist_directory='functions'))

collection = client.create_collection('functions')

for f in os.listdir('./functions'):
    path = os.path.join('./functions', f)
    with open(path, 'r') as f:
        func = json.load(f)

    embedding = get_embedding(func['description'])

    collection.add(
        documents=[json.dumps(func)],
        ids=[path],
        embeddings=[embedding])

client.persist()
