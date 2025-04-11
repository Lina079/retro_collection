from item import Item
from config import TYPES

def add_item():
    print("Adding an Item")
    print("--------------")
    title = input("Title> ")

    print("Types:")
    for key, value in TYPES.items():
        print(f"{key}. {value}")

    try:
        type_id = int(input("Type> "))
        if type_id not in TYPES:
            print("Invalid type.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    date_added = input("Date Added (DD/MM/YYYY)> ")
    date_made = input("Date of Manufacture (DD/MM/YYYY)> ")
    description = input("Description> ")

    Item(title, type_id, date_added, date_made, description)
    print("Item Added!")

def show_items_by_type():
    print("Types:")
    for key, value in TYPES.items():
        print(f"{key}. {value}")

    try:
        type_id = int(input("Type> "))
        if type_id not in TYPES:
            print("Invalid type.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    items = Item.get_all_by_type(type_id)
    print(f"\nShowing: {TYPES[type_id]}")
    print("_" * 50)
    for item in items:
        print(f"{item.title}\t{item.date_added}\t{item.date_made}")

def delete_item():
    items = Item.get_all_items()
    if not items:
        print("No items to delete.")
        return

    print("What would you like to delete?")
    for idx, item in enumerate(items):
        print(f"{idx + 1}. {item.title}")

    try:
        choice =  int(input("Delete> ")) - 1
        deleted = Item.delete_by_index(choice)
        if deleted:
            print(f"{deleted.title} Deleted")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")


def edit_item():
    items = Item.get_all_items()
    if not items:
        print("No items to edit.")
        return

    print("Which item would you like to edit?")
    for idx, item in enumerate (items):
        print(f"{idx + 1}. {item.title}")

    try:
        choice = int(input("Choice> ")) - 1
        if 0 <= choice < len(items):
            item = items[choice]
            print("Which field would you like to edit?")
            print("Options: title, type, date_added, date_made, description")
            field = input("Field> ").strip().lower()
            new_value = input("New value> ").strip()
            item.update_field(field, new_value)
            print("Item update successfully!")
        else:
            print("Invalid item number.")
    except ValueError:
        print("Please enter a valid number.")


def add_new_type():
    print("Adding a New Type")
    print("_________________")
    new_type = input("Enter new type name> ").strip()
    if new_type in TYPES.values():
        print("That type already exists.")
        return
    new_id = max(TYPES.keys()) + 1
    TYPES[new_id] = new_type
    print(f"Type '{new_type}' added successfully as option {new_id}.")

