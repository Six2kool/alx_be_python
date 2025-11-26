# Your epic shopping list manager!

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("-" * 25)

def main():
    shopping_list = []  # Empty list at the start!

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            # ADD ITEM
            item = input("What item do you want to add? ").strip()
            shopping_list.append(item)
            print(f"Added '{item}' to your list!")

        elif choice == '2':
            # REMOVE ITEM
            if not shopping_list:
                print("Your list is empty! Nothing to remove.")
            else:
                print("Current list:", shopping_list)
                item = input("Which item do you want to remove? ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"Removed '{item}' from your list!")
                else:
                    print(f"'{item}' not found in your list!")

        elif choice == '3':
            # VIEW LIST
            if not shopping_list:
                print("Your shopping list is empty! Time to add stuff!")
            else:
                print("\nYour Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                print(f"Total items: {len(shopping_list)}")

        elif choice == '4':
            print("Goodbye! Don't forget your stuff!")
            break

        else:
            print("Invalid choice! Please pick 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()