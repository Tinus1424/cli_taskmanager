from src.tasks import add_task, list_tasks
import argparse



def main():
    parser = argparse.ArgumentParser(description = "This is a taskmanager")
    parser.add_argument("-a", "--add", help="add task")
    parser.add_argument("-l", "--list", help="list tasks", action="store_true")
    args = parser.parse_args()
    if args.add: 
        add_task(args.add)
        print(f"Added '{args.add}' to the tasks list")
    if args.list:
        list_tasks()


if __name__ == "__main__":
    main()
