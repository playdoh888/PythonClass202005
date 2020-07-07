import json

simple_dictionary = [
    {
        "genre": "comedy",
        "name": "spaceballs"
    },
    {
        "genre": "tragedy",
        "name": "gone with the wind"
    },
    {
        "genre": "comedy",
        "name": "titanic"
    }
]

j = json.dumps(simple_dictionary, indent=4)
with open('sampleDICTIONARY2JSON.json', 'w') as f:
    f.write(j)
