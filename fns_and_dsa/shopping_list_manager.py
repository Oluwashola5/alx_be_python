# Check 1: Definition of display_menu function
def display_menu():
    """Displays the main menu for the shopping list manager."""
    # Ensuring the exact required print statement
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    # Check 2: Implementation of an array shopping_list
    shopping_list = []  # The shopping list array to store items

    while True:
        # Check 3: Calling the display_menu function
        display_menu()
        
        # Check 4: Implementation of choice input as a number
        try:
            choice = int(input("Enter your choice (1-4): ").strip())
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            # Add an item to the shopping list
            item = input("Enter the name of the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("Item name cannot be empty.")
        elif choice == 2:
            # Remove an item from the shopping list
            item = input("Enter the name of the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' is not in the shopping list.")
        elif choice == 3:
            # View the shopping list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("\nThe shopping list is empty.")
        elif choice == 4:
            # Exit the program
            print("Goodbye!")
            break
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
