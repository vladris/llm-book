from langchain.llms import OpenAI

llm = OpenAI()

response = llm.generate(['Say "Hello world" in Python.'])

print(response)
