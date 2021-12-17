class GroceryItem: 
  def __init__(self, name): 
    self.name = name 


class ShoppingList: 
  def __init__(self, name, address): 
    self.name = name 
    self.address = address 
    self.grocery_items = []

  def add_grocery_item(self, item):
    self.grocery_items.append(item)

  def delete_grocery_item(self, index):
    del self.grocery_items[int(index)]