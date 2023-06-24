import openai


def get_embedding(text):
    return openai.Embedding.create(
        input=[text.replace('\n', ' ')],
        model='text-embedding-ada-002')['data'][0]['embedding']
