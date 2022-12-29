import random
import json




def give_xp(amount: int= random.randint(0, 50)):
    with open('./data/xp.json', 'r') as f:
        rec = json.load(f)
    rec["xp"] = rec["xp"] + amount
    data = json.dumps(rec, indent=4)
    with open('./data/xp.json','w') as outfile:
        outfile.write(data)
    print(f"succesfully added {amount}exp!")

def remove_xp(amount: int= random.randint(0, 50)):
    with open('./data/xp.json', 'r') as f:
        rec = json.load(f)
    rec["xp"] = rec["xp"] - amount
    data = json.dumps(rec, indent=4)
    with open('./data/xp.json','w') as outfile:
        outfile.write(data)
    print(f"succesfully removed {amount}ex!p")
