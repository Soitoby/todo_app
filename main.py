import os  # python lib
import task_lib  # local lib
import termcolor, questionary  # type: ignore #download library


def check_folder(folder):
    if os.path.isdir(folder):
        return 0
    else:
        os.mkdir(folder)


def main():
    check_folder("task")
    run = True
    while run:

        choice = questionary.select(
            "What do you want to do?",
            choices=["create task", "watch task", "remove task","edit status","Close programm"]
        ).ask()
        try:
            match (choice):
                case "create task":
                    task_lib.create_task()
                case "watch task":
                    task_lib.watch_task()
                case "remove task":
                    task_lib.remove_task()
                case "Close programm":
                    run = False
                case "edit status":
                    task_lib.edit_status()
                case _:
                    print("uncorrect input")

        except TypeError:
            print(termcolor.colored("uncorrect type", "red"))
        except ValueError:
            print(termcolor.colored("pls input", "red"))


if __name__ == "__main__":
    main()

# 1.word watch task
# 2. remove task