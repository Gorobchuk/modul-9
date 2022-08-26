from typing import Dict, Callable
from contacts import book


def parser_handler(func):
    def wrapper(user_input: str):
        try:
            return func(user_input)
        except ValueError as e:
            return str(e)
        except KeyError as e:
            return str(e)

    return wrapper


@parser_handler
def hello_handler(*args):
    return "How can I help you?"


@parser_handler
def add_handler(username: str, number: str):
    if book.get(username) is None:
        book[username] = number
        return "Number was added"
    raise ValueError("Number already in book")


@parser_handler
def change_handler(username: str, number: str):
    if book.get(username) is not None:
        book[username] = number
        return "Number was changed"
    raise KeyError("Number does not exists")


@parser_handler
def phone_handler(username: str):
    phone = book.get(username)
    if phone is not None:
        return "User number is {phone}"
    raise ValueError


def show_all_handler(*args):
    all_response = "Book\n"
    contacts = "\n".join(
        f"{username} number is {number}" for (username, number) in book.items()
    )
    formatted_contacts = "Number does not exists, yet" if contacts == "" else contacts
    return all_response + formatted_contacts


def exit_handler(*args):
    raise SystemExit("Good bye")


def unknown_handler(*args):
    raise ValueError("Command is not valid!")


handlers: Dict[str, Callable] = {
    "hello": hello_handler,
    "add": add_handler,
    "change": change_handler,
    "phone": phone_handler,
    "show all": show_all_handler,
    "good bye": exit_handler,
    "close": exit_handler,
    "exit": exit_handler,
}
