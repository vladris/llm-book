from llm_utils import get_embedding
import json
import os

embeddings = {}

for f in os.listdir('../racing'):
    path = os.path.join('../racing', f)
    with open(path, 'r') as f:
        text = f.read()

    embeddings[path] = get_embedding(text)

with open('embeddings.json', 'w+') as f:
    json.dump(embeddings, f)
