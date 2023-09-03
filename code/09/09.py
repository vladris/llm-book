from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


class Fact(BaseModel):
    fact: str = Field(description='A fact about a subject.')
    reference: str = Field(description='A reference for the fact.')


parser = PydanticOutputParser(pydantic_object=Fact)

template = ChatPromptTemplate.from_messages([
    ('system', 'Your responses follow the format: {format}'),
    ('user', 'Tell me a fact about {subject}')
])

prompt = template.partial(format=parser.get_format_instructions())

llm = ChatOpenAI()

chain = prompt | llm | parser

print(chain.invoke({'subject': 'data scientists'}))
