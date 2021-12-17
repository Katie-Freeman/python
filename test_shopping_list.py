import unittest
from shoping_list import ShoppingList
from shoping_list import GroceryItem

class ShoppingListTest(unittest.TestCase): 
    
    def setUp(self):
        print("SETUP")
        self.shopping_list = ShoppingList("Kroger", "234 Road")
        self.shopping_list

    def test_add_grocery_item(self):
        self.shopping_list.add_grocery_item("banana")
        self.shopping_list.add_grocery_item("milk")
        self.assertEqual(2, len(self.shopping_list.grocery_items))

    def test_delete_grocery_item(self):
        self.shopping_list.add_grocery_item("banana")
        self.shopping_list.add_grocery_item("milk")
        self.shopping_list.delete_grocery_item(1)
        self.assertEqual(1, len(self.shopping_list.grocery_items))


    def tearDown(self):
        print("TEARDOWN")

if __name__ == '__main__':
    unittest.main()