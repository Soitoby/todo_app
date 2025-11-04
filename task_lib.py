import os
import termcolor, questionary # type: ignore


class task():
    def __init__(self, name,discription):
        self.name = name
        self.path = f"task/{name}/"
        self.discription = discription
        self.status = "create"
        file_create = ["discription.txt","status.txt"]
        text_create = [discription, "create"]
        for i in file_create,text_create:
            with open(f"{self.path}{i}","w") as f:
                f.write(text_create)

        print(termcolor.colored(f"create {name}", "green"))
        
    def edit_status(self, status):
        choice = questionary.select(
            "choose status", choice=["select","progress","done"]
        )   
        match (choice):
            case "select":
                pass
            case "progress":
                pass
            case "done":
                pass


def create_task():
    name = str(input("input name task:"))
    discription = str(input("input discription:"))
    status = "create"
    with open(f"task/{name}.txt", "w") as f:
        f.write(f"discription:{discription}\n")
        f.write(f"status:{status}")
    print("task create")

def watch_task():
    print()
    for i in os.listdir("task/"):
        print("\n",termcolor.colored(i,"red"))
        with open(f"task/{i}","r") as f:
            x = f.read().split()
            for i in range(len(x)):
                j = x[i].split(":")
                print(f"{termcolor.colored(j[0],"blue")}:{j[1]}")

            
    if input("return(Enter):") or True:
        return 0

def remove_task():
    list = os.listdir("task/")
    y = 0
    for i in list:
        print(f"{y}. {i}")
        y+=1
    x = input("why task done:")
    os.remove(f"task/{list[x]}")

def edit_status():
    pass