from handlers import handlers, unknown_handler
from parser import parse_user_input


def main():
    while True:
        user_input = input("Command: ")
        result = parse_user_input(user_input=user_input)
        if len(result) != 2:
            print(result)
            continue
        command, arguments = result
        command_handler = handlers.get(command, unknown_handler)
        try:
            command_response = command_handler(*arguments)
            print(command_response)
        except: SystemExit as e:
            print(str(e))
            break


if __name__ == "__main__":
    main()
