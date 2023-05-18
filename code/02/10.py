import tiktoken

enc = tiktoken.encoding_for_model('text-davinci-003')
tokens = enc.encode('Say "Hello world" in Python')

print(tokens)
print([enc.decode_single_token_bytes(token) for token in tokens])
