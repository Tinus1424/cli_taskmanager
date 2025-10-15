from src.tasks import add_task, list_tasks, remove_task, update_status
import argparse



def main():
    parser = argparse.ArgumentParser(description = "This is a taskmanager")
    parser.add_argument("-v", "--verbose", help="print additional information", action="store_true")
    parser.add_argument("-a", "--add", help="add task")
    parser.add_argument("-l", "--list", help="list tasks", action="store_true")
    parser.add_argument("-r", "--remove", help="remove tasks")
    parser.add_argument("-u", "--update", help="update the status of a task")
    parser.add_argument("-s", "--status", help="specificy a status for update")
    args = parser.parse_args()

    if args.add: 
        add_task(args.add, args.verbose)
    if args.list:
        list_tasks(args.verbose)
    if args.remove:
        remove_task(args.remove, args.verbose)
    if args.update:
        if not args.status:
            print("Please specify a status using -t")
            return
        update_status(args.update, args.status, args.verbose)

if __name__ == "__main__":
    main()
