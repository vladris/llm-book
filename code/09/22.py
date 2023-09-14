import asyncio
import os
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel.orchestration.sk_context import SKContext
from semantic_kernel.planning.sequential_planner.sequential_planner import SequentialPlanner
from semantic_kernel.skill_definition import sk_function, sk_function_context_parameter

kernel = sk.Kernel()
kernel.add_chat_service('chat_completion', OpenAIChatCompletion(
    'gpt-3.5-turbo', os.environ['OPENAI_API_KEY']))

class CalendarPlugin:
    @sk_function(
        description='Gets the email addresses of a user given their name',
        name='get_email'
    )
    @sk_function_context_parameter(
        name='name',
        description='A name for which to return the email address'
    )
    def get_email(self, context: SKContext) -> str:
        print(f'* Getting email for {context["name"]}')

        address_book = {
            'John Doe': 'john.doe@example.com',
            'Jane Doe': 'jane.doe@example.com',
        }

        return address_book[context['name']]


    @sk_function(
        description='Sends a meeting invitation with the given subject to the given recipient emails at the given time',
        name='schedule_meeting'
    )
    @sk_function_context_parameter(
        name='input',
        description='Recipient email for the meeting invitation'
    )
    @sk_function_context_parameter(
        name='subject',
        description='Meeting subject'
    )
    @sk_function_context_parameter(
        name='location',
        description='Meeting location'
    )
    @sk_function_context_parameter(
        name='time',
        description="Meeting time"
    )
    def schedule_meeting(self, context: SKContext) -> str:
        print(f"* Meeting '{context['subject']}' at '{context['location']}' scheduled for {context['time']} with {context['input']}")
        return 'Success'


calendar_plugin = kernel.import_skill(CalendarPlugin(), 'calendar')

ask = 'Schedule lunch with Jane Doe for Monday at noon at Tipsy Cow'

planner = SequentialPlanner(kernel)
plan = asyncio.run(planner.create_plan_async(goal=ask))

for index, step in enumerate(plan._steps):
    print("Function: " + step.skill_name + "." + step._function.name)
    print("Input vars: " + str(step.parameters.variables))
    print("Output vars: " + str(step._outputs))

result = asyncio.run(plan.invoke_async())
print(result.result)
