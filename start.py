from back import frequency_handler, todos, xp
import threading
import json

# STRUCTS

TODOS = {

}

XP = {
    "xp": 0
}

# TEMPLATING

try:
    with open('./data/todos.json', 'r') as f:
        todos_dict = json.load(f)
    with open('./data/xp.json', 'r') as f:
        xp_dict = json.load(f)
    print('ALREADY INITIALIZED!')
except:
    TODOS_dict = json.dumps(TODOS, indent=4)
    XP_dict = json.dumps(XP, indent=4)
    with open('./data/todos.json', 'w') as outfile:
        outfile.write(TODOS_dict)
    with open('./data/XP.json', 'w') as outfile:
        outfile.write(XP_dict)
    print("INITIALIZED!")

# SUB PROCESS
t = threading.Thread(target=frequency_handler.frequency)
t.start()

