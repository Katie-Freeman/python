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

  def delete_grocery_item(self, index):
    del self.grocery_items[int(index)]

  def display_all_shopping_lists():
    for index in range(0, len(shopping_lists)):
        shopping_list = shopping_lists[index]
        print("===============")
        print(f"{shopping_list.name}")
        print("===============")
        for index in range(0, len(shopping_list.grocery_items)):
            print(f"{index+1}.{shopping_list.grocery_items[index].name}")