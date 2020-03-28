import sys
from . go import Go


def main():
    args = sys.argv[1:]
    handler = Go()

    if len(args) == 0:
        handler.help()
    elif args[0] == "help" or args[0] == "h":
        handler.help()
    elif args[0] == "add":
        if(len(args) == 1):
            print("No name provided, use 'go help' for help")
        if(len(args) == 3):
            handler.add(args[1], args[2])
        else:
            handler.add(args[1])
    elif args[0] == "remove":
        if len(args) == 1:
            print("No name provided, use 'go help' for help")
        else:
            handler.remove(args[1])
    elif args[0] == "all":
        handler.all()
    else:
        handler.go(args[0])


if __name__ == '__main__':
    main()