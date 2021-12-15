
shopping_list = []

class GroceryItem:
    def __init__(self, name):
        self.name = name

class ShoppingList:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.grocery_items = []
    
    def add_grocery_item(self, item):
        self.grovery_items.append(item)

def display_all_shopping_lists(): 
    for index in range(0, len(shopping_lists)):
       shopping_list = shopping_lists[index]
       print(f"{index}. {shopping_list.name}")
  
print("1. Add a shopping list")
print("2. add item to an existing shopping list")
print("3. display shopping lists")
print("q to quit")

choice = input("Enter choice: ")

if choice == "1":
    display_all_shopping_lists()
    name = input("Enter name of shopping list: ")
    address = input("Enter shopping list address: ")
    shopping_list = ShoppingList(name, address)
    shopping_lists.append(shopping_list)
elif choice == "3":
    display_all_shopping_lists()