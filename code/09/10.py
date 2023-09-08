from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader, DirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.vectorstores import Chroma

loader = DirectoryLoader('../racing', loader_cls=TextLoader)
docs = loader.load()
db = Chroma.from_documents(docs, OpenAIEmbeddings())

retriever = db.as_retriever(search_kwargs={'k': 1})

template = ChatPromptTemplate.from_messages([
    ('system', 'Your are a Q&A AI.'),
    ('system',
     'Here are some facts that can help you answer the following question: {data}'),
    ('user', '{prompt}')
])

llm = ChatOpenAI()

chain = {'data': retriever, 'prompt': RunnablePassthrough()} | template | llm


while True:
    prompt = input('user: ')
    if prompt == 'exit':
        break

    print(chain.invoke(prompt).content)
