import json
import back.xp


def create_todo(title: str, value: str=""):
    with open('./data/todos.json', 'r') as f:
        rec = json.load(f)

    if title != "" or " " and title not in rec:
        rec[title] = {"value": value, "status": 0}
        with open('./data/todos.json', 'w') as outfile:
            data = json.dumps(rec, indent = 4)
            outfile.write(data)
        print(f"added Todo:", title)
        back.xp.give_xp()
    else:
        print("ERROR: TITLE ALREADY EXISTS OR WRONG VALUES!")


def delete_todo(title: str):
    with open('./data/todos.json', 'r') as f:
        rec = json.load(f)
    if title in rec:
        del rec[title]
        data = json.dumps(rec, indent=4)
        with open('./data/todos.json', 'w') as outfile:
            outfile.write(data)
        print("Successfully deleted:", title)
        back.xp.remove_xp()
        print("Dont get your goals underestimated!")
    else:
        print("ERROR: such title doesnt exist!")

# delete_todo("hi")

def edit_todo(title: str, edited: int, edited_text: str):
    with open('./data/todos.json', 'r') as f:
        rec = json.load(f)
    if title in rec and rec[title]:
        if edited == 0:
            rec[edited_text] = rec[title]
            del rec[title]
            data = json.dumps(rec, indent=4)
            with open('./data/todos.json', 'w') as outfile:
                outfile.write(data)
            print("Edited Title!")
            back.xp.give_xp(15)
        elif edited == 1:
            rec[title]["value"] = edited_text
            data = json.dumps(rec, indent=4)
            with open('./data/todos.json', 'w') as outfile:
                outfile.write(data)
            print("Edited value!")
            back.xp.give_xp(15)

    else:
        print("ERROR: such title doesnt exist!")
# edit_todo("hi2", 1, "Still nodelete")
# edit_todo("hi", 0, "Hi(edited)")

def mark_as_done(title: str):
    with open('./data/todos.json', 'r') as f:
        rec = json.load(f)
    if title in rec:
        rec[title]["status"] = 1
        data = json.dumps(rec, indent=4)
        with open('./data/todos.json', 'w') as outfile:
            outfile.write(data)
        print("marked as done")
        back.xp.give_xp(100)

