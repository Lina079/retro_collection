from collection import add_item, show_items_by_type, delete_item, edit_item, add_new_type
from storage import load_items, save_items, load_types

def show_menu():
    print("\nPython Collector")
    print("__________________")
    print("1. Add Item to Collection.")
    print("2. Show Items in Collection.")
    print("3. Delete Items from Collection.")
    print("4. Edit Item in Collection.")
    print("5. Add New Item Type.")
    print("6. Exit")

def main():
    load_types()
    load_items()


    while True:
        show_menu()
        choice = input("Choice> ")

        if choice =="1":
            add_item()
        elif choice == "2":
            show_items_by_type()
        elif choice == "3":
            delete_item()
        elif choice == "4":
            edit_item()
        elif choice == "5":
            add_new_type()
        elif choice == "6":
            save_items()
            print("Goodbye!")
            break
        else:
            print("Invalid choice, Please choose 1-6.")


if __name__ == "__main__":
    main()