from shoping_list import ShoppingList
from shoping_list import GroceryItem

shopping_lists = []
    

def display_all_shopping_lists():
    for index in range(0, len(shopping_lists)):
        shopping_list = shopping_lists[index]
        print("===============")
        print(f"{shopping_list.name}")
        print("===============")
        for index in range(0, len(shopping_list.grocery_items)):
            print(f"{index+1}.{shopping_list.grocery_items[index].name}")
    

def main():
    
    while True:
        try:
            print("1. Add a shopping list")
            print("2. Add item to an existing shopping list")
            print("3. Display shopping lists")
            print("4. Delete an item from shopping list")
            print("q to quit")
            
            choice = input("Enter choice: ")
            if choice == "1": 
                display_all_shopping_lists() 
                name = input("Enter name of shopping list: ")
                address = input("Enter shopping list address: ")
                    
                shopping_list = ShoppingList(name, address)
                shopping_lists.append(shopping_list)
            
            elif choice == "2":
                try:
                    print("Which list would you like to add to?")
                    display_all_shopping_lists()
                    list_choice = int(input ("Enter Choice: "))
                    shopping_list = shopping_lists[list_choice -1]

                    name = input("Enter grocery item: ")
                    grocery_item = GroceryItem(name)

                    shopping_list.add_grocery_item(grocery_item)
                except ValueError:
                    print("Please select a number")

            elif choice == "3":
                display_all_shopping_lists()

            elif choice == "4":
                try:
                    display_all_shopping_lists()
                    list_choice = int(input ("Enter choice: "))
                    shopping_list = shopping_lists[list_choice -1]
                    item_choice = int(input ("Enter item choice: "))
                    shopping_list.delete_grocery_item(item_choice -1)
                    display_all_shopping_lists()
                except ValueError:
                    print("Please select a number")


            elif choice == "q":
                break

        except IndexError:
            print("This is not a valid selection")
    


main()