from langchain.chains import LLMChain, TransformChain, SequentialChain
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

llm_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    output_key='json')

transformer_chain = TransformChain(
    input_variables=['json'],
    output_variables=['fact'],
    transform=lambda inp: {'fact': parser.parse(inp['json'])})

chain = SequentialChain(
    input_variables=['subject'],
    chains=[llm_chain, transformer_chain])

print(chain.run(subject='data scientists'))
