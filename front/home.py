import json
from pick import pick

with open('./data/todos.json', 'r') as f:
    todos = json.load(f)

for todo in todos:
    options = todo

index, option = pick(options, indicator="=>")
print(index)