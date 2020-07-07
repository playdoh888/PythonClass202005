import requests, json

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

for i in todos:
    print(i)
