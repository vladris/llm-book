from llm_utils import ChatTemplate

chat = ChatTemplate({
    'messages': [
        {'role': 'user', 'content': 'What is the weather like today in Seattle?'},
        {'role': 'function', 'name': 'get_weather', 'content': 'Sunny and 75 degrees, with 10% chance of rain.'}],
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
