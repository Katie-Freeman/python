
shopping_lists = [] 

class GroceryItem: 
  def __init__(self, name): 
    self.name = name 


class ShoppingList: 
  def __init__(self, name, address): 
    self.name = name 
    self.address = address 
    self.grocery_items = []
  def __str__(self):
        return ""
  
  def add_grocery_item(self, item):
    self.grocery_items.append(item)
    

def display_all_shopping_lists():
    for index in range(0, len(shopping_lists)):
        shopping_list = shopping_lists[index]
        print("===============")
        print(f"{shopping_list.name}")
        print("===============")
        for index in range(0, len(shopping_list.grocery_items)):
            print(f"{index+1}.{shopping_list.grocery_items[index].name}")
    

def print_menu_error():
    print("That was not a valid choice. Try again. \n\n\n")

def main():
    
    while True:

        print("1. Add a shopping list")
        print("2. Add item to an existing shopping list")
        print("3. Display shopping lists")
        print("q to quit")

        choice = input("Enter choice: ")

        if choice == "1": 
            display_all_shopping_lists() 
            name = input("Enter name of shopping list: ")
            address = input("Enter shopping list address: ")
            
            shopping_list = ShoppingList(name, address)
            shopping_lists.append(shopping_list)
        
        elif choice == "2":
            print("Which list would you like to add to?")
            display_all_shopping_lists()
            list_choice = int(input ("Enter choice: "))
            shopping_list = shopping_lists[list_choice -1]

            name = input("Enter grocery item: ")
            grocery_item = GroceryItem(name)

            shopping_list.add_grocery_item(grocery_item)

        elif choice == "3":
            display_all_shopping_lists()
           
        elif choice == "q":
            break
main()