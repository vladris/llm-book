from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

llm = ChatOpenAI()

response = llm([HumanMessage(content='Say "Hello world" in Python.')])

print(response)
