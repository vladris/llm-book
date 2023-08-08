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

#...

chat = ChatTemplate({
    'temperature': 0,
    'messages': [{'role': 'system', 'content': 'You are a large language model generating detailed and granular plans to achieve complex goals. Come up with a multiple step plan that will achieve the given goal. Output these steps as a JSON array with the format {"Thought": <Reasoning behind the step and recall choices>, "Step": <Large language model prompt for the step>, "Recall": [<Useful output of previous steps to make available to this step (maximum 3)>]}.'},
                    {'role': 'system', 'content': 'You have the following functions you can call: `search_expedia(query)` to search Expedia and `search_kayak(query)` to search Kayak. You can call a function by responding with just the function name and argument. When you have enough data to complete the Step, respond with `return(result)` where result is the answer for the step as a string. Your output should be just function calls, no additional explanations.'},
                    {'role': 'user', 'content': goal},
                    {'role': 'assistant', 'content': json.dumps(plan)},
                    {'role': 'user', 'content': 'There was an error executing Step 2 of the plan: `search_kayak encountered an unknown error`. Rewrite the plan to exclude this step.'}]})

print(chat.completion({}).choices[0].message.content)