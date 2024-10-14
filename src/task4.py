def parse_input(user_input):
    if not user_input:
        return None, None
    if " " not in user_input:
        return normalize_input(user_input), None

    cmd, *args = user_input.split()
    cmd = normalize_input(cmd)
    print('cmd', cmd)
    return cmd, *args


def normalize_input(user_input):
    return user_input.strip().lower()


def add_contact(args, contacts):
    name, phone = args

    contacts[name] = phone
    return "Contact added."


def all_contacts(contacts):
    return contacts


def change_username_phone(args, contacts):
    name, phone = args
    contacts[name] = phone if name in contacts else None
    return f"Contact changed, new contact is: {name} - {phone}."


def phone_by_name(args, contacts):
    print('args', args)
    name = args[0]

    return contacts.get(name, "Contact not found.")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if not command:
            print("Invalid command.")
            continue
        if not args:
            print("Invalid arguments.")
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":
            print(all_contacts(contacts))
        elif command == "change":
            print(change_username_phone(args, contacts))
        elif command == "phone":
            print(phone_by_name(args, contacts))
        elif command == "phone":
            print(phone_by_name(args, contacts))
        elif command == "help":
            print("Commands: hello, add, all, change, phone, close, exit, help")
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
