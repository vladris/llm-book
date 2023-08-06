from llm_utils import ChatTemplate
import json

example_plan = [
    {'Thought': 'In order to write a sci-fi novella, I need to first come up with a plot and characters.',
     'Step': 'Step 1: Brainstorm ideas for the plot and characters of the science fiction novella focusing on AI ethics.',
     'Recall': []},
    {'Thought': 'I need to expand the plot idea into an outline. I need to recall the plot idea (Step 1).',
     'Step': 'Step 2: Create an outline for the three chapters, ensuring a clear structure and progression of the theme.',
     'Recall': ['Step 1']},
    {'Thought': 'I need to develop the main characters. I need to recall the character ideas (Step 1) and plot outline (Step 2).',
     'Step': 'Step 3: Develop the main characters, including an AI protagonist and human characters affected by the AI\'s actions.',
     'Recall': ['Step 1', 'Step 2']},
    {'Thought': 'I will write one chapter at a time, so I will start with chapter 1. I need to recall the outline (Step 2) and characters (Step 3).',
     'Step': 'Step 4: Write chapter 1 according to the outline.',
     'Recall': ['Step 2', 'Step 3']},
    {'Thought': 'I will continue with chapter 2, I need to recall the outline (Step 2), characters (Step 3), and the previous chapter (Step 4)',
     'Step': 'Step 5: Write chapter 2 according to the outline.',
     'Recall': ['Step 2', 'Step 3', 'Step 4']},
    {'Thought': 'I will continue with chapter 3, I need to recall the outline (Step 2), characters (Step 3), and, since I can only recall one additional output, I will recall the previous chapter (Step 5)',
     'Step': 'Step 6: Write chapter 3 according to the outline.',
     'Recall': ['Step 2', 'Step 3', 'Step 5']}]

chat = ChatTemplate({
    'messages': [
        {'role': 'system',
            'content': 'You are a large language model generating detailed and granular plans to achieve complex goals. Come up with a multiple step plan that will achieve the given goal. Output these steps as a JSON array with the format {"Thought": <Reasoning behind the step and recall choices>, "Step": <Large language model prompt for the step>, "Recall": [<Useful output of previous steps to make available to this step (maximum 3)>]}.'},
        {'role': 'user', 'content': 'Write a short 3 chapter sci-fi novella on the theme of AI ethics.'},
        {'role': 'assistant', 'content': json.dumps(example_plan)},
        {'role': 'system',
            'content': 'You have the following functions you can call: `search_expedia(query)` to search Expedia and `search_kayak(query)` to search Kayak. You can call a function by responding with just the function name and argument. This will give you the response.'},
        {'role': 'user', 'content': 'Find the cheapest flight from Seattle to Los Angeles and return it to the user.'}]})

print(chat.completion({}).choices[0].message.content)
