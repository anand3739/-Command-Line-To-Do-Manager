import argparse
import os

TASK_FILE = "tasks.txt"
# Ensure the task file exists
if not os.path.exists(TASK_FILE):
    open(TASK_FILE, 'w').close()

def add_task(task):
    with open(TASK_FILE, 'a') as file:
        file.write(task + '\n')
    print(f" Task added: {task}")

def view_tasks():
    with open(TASK_FILE, 'r') as file:
        tasks = file.readlines()
    
    if not tasks:
        print(" No tasks found.")
        return

    print(" Your To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task.strip()}")

def delete_task(task_number):
    with open(TASK_FILE, 'r') as file:
        tasks = file.readlines()

    if task_number < 1 or task_number > len(tasks):
        print(" Invalid task number.")
        return

    removed = tasks.pop(task_number - 1)

    with open(TASK_FILE, 'w') as file:
        file.writelines(tasks)

    print(f" Task deleted: {removed.strip()}")

def main():
    parser = argparse.ArgumentParser(description="Simple CLI To-Do List Manager")
    subparsers = parser.add_subparsers(dest='command')

    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('task', type=str, help='Task description')

    # View command
    subparsers.add_parser('view', help='View all tasks')

    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a task by number')
    delete_parser.add_argument('number', type=int, help='Task number to delete')

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.task)
    elif args.command == 'view':
        view_tasks()
    elif args.command == 'delete':
        delete_task(args.number)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
