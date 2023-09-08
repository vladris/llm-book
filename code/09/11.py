from langchain.agents import AgentExecutor, OpenAIFunctionsAgent, tool
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage


@tool
def get_emails(names):
    """Get the email addresses of a set of users given their names"""
    print(f'* Getting emails for {names}')

    address_book = {
        'John Doe': 'john.doe@example.com',
        'Jane Doe': 'jane.doe@example.com',
    }
    emails = {}

    for name in names:
        emails[name] = address_book[name]

    return emails


@tool
def schedule_meeting(subject, recipients, time):
    """Sends a meeting invitation with the given subject to the given recipient emails at the given time"""

    print(f"* Meeting '{subject}' scheduled for {time} with {recipients}")
    return {'success': True}


tools = [get_emails, schedule_meeting]

system_message = SystemMessage(content="You are an AI personal assistant.")

prompt = OpenAIFunctionsAgent.create_prompt(system_message=system_message)

llm = ChatOpenAI()

agent = OpenAIFunctionsAgent(llm=llm, tools=tools, prompt=prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
agent_executor.run(
    'Schedule lunch with Jane Doe for Monday at noon at Tipsy Cow')
