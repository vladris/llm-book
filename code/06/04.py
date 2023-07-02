from llm_utils import ChatTemplate

chat = ChatTemplate({
    'messages': [{'role': 'user', 'content': 'What is the weather like today in Seattle?'}],
    'functions': [
        {
            "name": "get_weather",
            "description": "Gets the weather given a city name",
            "parameters": {
                "type": "object",
                "properties": {"city": {"type": "string"}}
            }
        }]})

print(chat.completion({}).choices[0])
