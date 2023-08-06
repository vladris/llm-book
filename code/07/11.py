import json


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
