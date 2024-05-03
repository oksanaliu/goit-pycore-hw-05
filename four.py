import json

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid command."

    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    save_contacts(contacts)
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        save_contacts(contacts)
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def get_phone(args, contacts):
    if not args:
        raise ValueError("Enter the argument for the command")
    
    name = args[0]
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        return "Contact not found."

@input_error
def display_all_contacts(contacts):
    if not contacts:
        return "No contacts found."
    else:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = load_contacts()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip().lower()

        if user_input in ["close", "exit"]:
            print("Good bye!")
            break
        elif user_input == "hello":
            print("How can I help you?")
        elif user_input.startswith("add"):
            _, *args = user_input.split(maxsplit=2)
            print(add_contact(args, contacts))
        elif user_input.startswith("change"):
            _, *args = user_input.split(maxsplit=2)
            print(change_contact(args, contacts))
        elif user_input.startswith("phone"):
            _, *args = user_input.split(maxsplit=1)
            print(get_phone(args, contacts))
        elif user_input == "all":
            print(display_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()