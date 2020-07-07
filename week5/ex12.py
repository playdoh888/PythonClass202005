import json

with open('SamplePeople.json') as f:
  data = json.load(f)

for i in data:
  print(i)

for j in data['users']:
  print(j)