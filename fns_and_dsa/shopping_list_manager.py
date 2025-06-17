

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    #initialize empty list 
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ") #prompt for an item
            shopping_list.append(item) # adding item to shopping list

        elif choice == '2':
            item1 = input("Please enter the item to be removed: ") #prompt for the item to be removed
            while item1 in shopping_list: #check to see if item is present in list
                shopping_list.remove(item1) #remove item from shopping list

        elif choice == '3':
            print(f'{shopping_list}') #display the shopping list

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()