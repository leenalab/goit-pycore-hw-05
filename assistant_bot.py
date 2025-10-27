# створюємо асистент-бота, який приймає команди від користувача
# і виконує відповідні дії

# Створити функцію main(), яка буде управляти основним ціклом бота
# Ствоити функцую parse_input(), яка буде розбирати введені користувачем дані на команди
# та аргументи

# Cтворити функції обробники для різних команд, такі як hello, add_contact(), 
# change_contact(), show_phone(), show_all(), close()

# програма повинна ідентифікувати та повідомляти про неправильно введені команди.

def parse_input(user_input: str): # робимо парсер (розбір) вводу

    parts = user_input.strip().split()
    if not parts:                 # якщо рядок порожній
        return "", []             # повертаємо "порожню" команду
    cmd, *args = parts
    return cmd.lower(), args

def add_contact(args: list[str], contacts: dict) -> str: # додаємо контакт
    # очікуємо рівно 2 аргументи: ім'я та телефон
    if len(args) != 2:
        return "Invalid contact details format. Use: add <name> <phone>"
    name, phone = args
    key = name.lower()
    contacts[key] = {"name": name, "phone": phone}
    return f"Contact {name} added."

def change_contact(args: list[str], contacts: dict) -> str: # змінюємо контакт
    # очікуємо рівно 2 аргументи: ім'я та новий телефон
    if len(args) != 2:
        return "Invalid format. Use: change <name> <new_phone>"
    name, new_phone = args
    key = name.lower()
    if key in contacts:
        contacts[key]["phone"] = new_phone
        return f"Phone number for {contacts[key]['name']} changed to {new_phone}."
    else:
        return f"Contact '{name}' not found."
    
def show_phone(args: list[str], contacts: dict) -> str:
    if len(args) != 1:
        return "Invalid format. Use: phone <name>"
    name = args[0]
    key = name.lower()
    if key in contacts:
        return f"{contacts[key]['name']}'s phone number is {contacts[key]['phone']}."
    else:
        return f"Contact '{name}' not found."
    
def show_all(contacts: dict) -> str: # показуємо всі контакти
    if not contacts:
        return "Your contact list is empty."
    lines = ["Contact list:"]
    for rec in sorted(contacts.values(), key=lambda r: r["name"].lower()):
        lines.append(f"• {rec['name']}: {rec['phone']}")
    return "\n".join(lines)


def main():
    contacts = {}  # словник для збереження контактів
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: hello, add, change, phone, all, close, exit\n").strip()
        command, args = parse_input(user_input)

        if command in ["close", "exit"]: # вихід з програми
            print("Good bye!")
            break

        elif command in ["hello", "hi", "hey"]: # привітання
            print("How can I help you?")

        elif command == "add": # додати контакт
            # просимо одразу ввести дані контакту
            print("Please, give us your user contact details: name, phone")
            details = input("Enter name and phone separated by comma, space: ").replace(",", "").strip()
            args = details.split()
            print(add_contact(args, contacts))

            

        elif command == "change": # змінити контакт

            print("Please, enter contact to change: name, new_phone")
            details = input("Enter name and new phone separated by comma, space: ").replace(",", "").strip()
            args = details.split()
            print(change_contact(args, contacts)) 

            
        
        elif command == "phone": # показати номер телефону
            if len(args) == 0:
                print("Please, enter the contact name to look up.")
                details = input("Enter contact name: ").strip()
                args = [details]
            print(show_phone(args, contacts))
           
        elif command == "all":
            print(show_all(contacts))

        elif command == "":
            # порожній ввід – просто питаємо ще раз, без "Invalid command."
            continue
        else:
            print("Invalid command.")
if __name__ == "__main__":
    main()





