"""# створюємо асистент-бота, який приймає команди від користувача
# і виконує відповідні дії

# Створити функцію main(), яка буде управляти основним ціклом бота
# Ствоити функцую parse_input(), яка буде розбирати введені користувачем дані на команди
# та аргументи

# Cтворити функції обробники для різних команд, такі як hello, add_contact(), 
# change_contact(), show_phone(), show_all(), close()

# програма повинна ідентифікувати та повідомляти про неправильно введені команди.
"""
from functools import wraps
# додаємо Import wraps - для використовування декораторів

def input_error(func): # нова функція декоратор
    
    @wraps(func) # додаємо декоратор із модуля functools, для збереження метаданних орігінальної функції (func) 
    def inner(*args, **kwargs): # функція обгортка, ловимо помилки
        try:
            return func(*args, **kwargs) 
        except KeyError:
            return "Contact not found." # ловимо помилки
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Not enough arguments."
    return inner     # повертаємо обгортку замість ориг. функції




def parse_input(user_input: str): 

    parts = user_input.strip().split()
    if not parts:                 
        return "", []             
    cmd, *args = parts
    return cmd.lower(), args


@input_error # додаємо декоратор

def add_contact(args, contacts): # додаємо контакт

    """if len(args) != 2:
        return "Invalid contact details format. Use: add <name> <phone>""" 
    # Прибрали, тепер це замінює декоратор @input_error і ловить помилку ValueError
    name, phone = args
    key = name.lower()  # приводимо ім’я до нижнього регістру
    contacts[key] = {"name": name, "phone": phone}  # додаємо структурований запис для гнучкості
    return f"Contact {name} added."
    
@input_error # додаємо декоратор

def change_contact(args, contacts): # змінюємо контакт
    # очікуємо рівно 2 аргументи: ім'я та новий телефон
    """if len(args) != 2:
        return "Invalid format. Use: change <name> <new_phone>" """
    # Прибрали, тепер це замінює декоратор @input_error і ловить помилку ValueError
    name, new_phone = args
    key = name.lower()
    if key not in contacts:
        # спеціально даємо KeyError, щоб повідомлення прийшло з декоратора
        raise KeyError(name)
    contacts[key]["phone"] = new_phone
    return f"Phone number for {contacts[key]['name']} changed to {new_phone}."

@input_error # додаємо декоратор        
def show_phone(args, contacts):
    """if len(args) != 1:
        return "Invalid format. Use: phone <name>" """
    # якщо немає аргументу -> IndexError (декоратор)
    name = args[0]
    key = name.lower()
    rec = contacts[key]          # якщо контакту нема -> KeyError (декоратор)
    return f"{rec['name']}'s phone number is {rec['phone']}."
    
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





