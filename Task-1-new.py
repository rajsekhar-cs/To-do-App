#!/usr/bin/env python
# coding: utf-8

# In[1]:


TASK_FILE = "tasks.txt"


def load_tasks():
    tasks = []

    try:
        with open(TASK_FILE, "r") as file:
            for line in file:
                line = line.strip()

                if line:
                    status, task = line.split("|", 1)
                    tasks.append({"task": task, "done": status == "1"})

    except FileNotFoundError:
        pass

    return tasks



def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for item in tasks:
            status = "1" if item["done"] else "0"
            file.write(f"{status}|{item['task']}\n")



def show_tasks(tasks):
    print("\n===== TASK LIST =====")

    if not tasks:
        print("No tasks available.")
        return

    for index, item in enumerate(tasks, start=1):
        status = "✓" if item["done"] else "✗"
        print(f"{index}. [{status}] {item['task']}")



def add_task(tasks):
    task = input("Enter new task: ")

    tasks.append({"task": task, "done": False})

    save_tasks(tasks)

    print("Task added successfully!")



def remove_task(tasks):
    show_tasks(tasks)

    try:
        number = int(input("Enter task number to remove: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks(tasks)
            print(f"Removed task: {removed['task']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")



def complete_task(tasks):
    show_tasks(tasks)

    try:
        number = int(input("Enter task number to mark as complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["done"] = True
            save_tasks(tasks)
            print("Task marked as complete!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")



def main():
    tasks = load_tasks()

    while True:
        print("\n===== TASK MANAGER =====")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Complete")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            remove_task(tasks)

        elif choice == "4":
            complete_task(tasks)

        elif choice == "5":
            print("Exiting Task Manager...")
            break

        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()



# In[ ]:




