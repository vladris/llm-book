from llm_utils import ChatTemplate
import json

goal = 'Find the cheapest flight from Seattle to Los Angeles'
plan = [
    {'Thought': 'To find the cheapest flight from Seattle to Los Angeles, I can search Expedia and Kayak.',
        'Step': 'Step 1: Search for flights from Seattle to Los Angeles on Expedia.', 'Recall': []},
    {'Thought': 'I will now search for flights from Seattle to Los Angeles on Kayak to compare prices.',
     'Step': 'Step 2: Search for flights from Seattle to Los Angeles on Kayak.', 'Recall': []},
    {'Thought': 'To return the cheapest flight to the user, I need to compare the results from both Expedia and Kayak. I need to recall the results from both searches (Step 1 and Step 2).', 'Step': 'Step 3: Compare the results from both searches and return the cheapest flight to the user.', 'Recall': [
        'Step 1', 'Step 2']}
]


def search_expedia(query):
    return json.dumps([
        {'time': '5:30 AM', 'airline': 'Delta', 'price': '$220'},
        {'time': '15:00 PM', 'airline': 'Alaska', 'price': '$170'},
        {'time': '17:30 PM', 'airline': 'Delta', 'price': '$140'}])


def search_kayak(query):
    if 'Seattle' in query:
        return '"Seattle" is not a valid airport code. Did you mean "SEA"?'
    elif 'Los Angeles' in query:
        return '"Los Angeles" is not a valid airport code. Did you mean "LAX"?'
    else:
        return json.dumps([
            {'time': '5:30 AM', 'airline': 'Delta', 'price': '$220'},
            {'time': '11:00 AM', 'airline': 'Alaska', 'price': '$160'},
            {'time': '15:00 PM', 'airline': 'Alaska', 'price': '$170'}])


def function_call(response):
    if response.startswith('search_expedia('):
        return False, search_expedia(response[15:-1])
    elif response.startswith('search_kayak('):
        return False, search_kayak(response[13:-1])
    elif response.startswith('return('):
        return True, response[7:-1]
    else:
        return False, 'Error - response should be a function call.'


def execute_step(step, template):
    print(step['Step'])

    turn = 1
    while turn <= 5:
        response = chat.completion({}).choices[0].message.content
        done, value = function_call(response)
        if done:
            return value

        chat.template['messages'].append(
            {'role': 'assistant', 'content': response})
        chat.template['messages'].append(
            {'role': 'user', 'content': value})

        print(f'> {response}')
        print(f'{value}')

        turn += 1

    raise Exception('Turn limit exceeded')


memory = {}
for i, step in enumerate(plan):
    chat = ChatTemplate({
        'temperature': 0,
        'messages': [{'role': 'system',
                      'content': 'You have the following functions you can call: `search_expedia(query)` to search Expedia and `search_kayak(query)` to search Kayak. You can call a function by responding with just the function name and argument. When you have enough data to complete the Step, respond with `return(result)` where result is the answer for the step as a string. Your output should be just function calls, no additional explanations.'},
                     {'role': 'system',
                      'content': step['Step']}]})

    for recall in step['Recall']:
        chat.template['messages'].append(
            {'role': 'system', 'content': f'Here is some information that will help you: {memory[recall]}'})

    result = execute_step(step, chat)
    memory[f'Step {i+1}'] = f'{step["Step"]} result is `{result}`'

print(f'Final result: {result}')
