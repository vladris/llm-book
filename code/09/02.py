from langchain.llms import OpenAI

llm = OpenAI()

response = llm('Say "Hello world" in Python.')

print(response)
