import os
import termcolor, questionary


def choose_task():
    if os.path.isdir("task/"):
        list = os.listdir("task/")
    else:
        return print(termcolor.colored("zero task", "red"))
    
    choice_file = questionary.select("choose task?", choices=list).ask()
    return choice_file

def create_task():
    name_task = input("input name task:")
    discription = input("input discription:")
    path = f"task/{name_task}"
    os.mkdir(path)

    file_create = ["discription.txt", "status.txt"]
    file_write = [discription, "create"]

    x = 0
    for i in file_create:
        with open(f"{path}/{i}", "x") as f:
            f.write(file_write[x])
        x += 1

    print(termcolor.colored(f"create {name_task}", "green"))


def edit_status():
    with open(f"task/{choose_task()}/status.txt","w") as f:
        choice_status = questionary.select("choose status:", choices=["select","progress","done"]).ask()
        f.write(choice_status)
    
    return print(termcolor.colored("edit status done", "green"))

def remove_task():
    task = choose_task()
    for i in os.listdir(f"task/{task}"):
        os.remove(f"task/{task}/{i}")
    os.rmdir(f"task/{task}")
    print(termcolor.colored("delete task","green"))

def watch_task():
    task = choose_task()
    for i in os.listdir(f"task/{task}"):
        with open(f"task/{task}/{i}","r") as f:
            if i == "discription.txt":
                print(termcolor.colored("discription: ","blue"), f.read())                
            if i == "status.txt":
                print(termcolor.colored("status: ","blue"), f.read())
    if input("back(enter)") or True: return 0
        