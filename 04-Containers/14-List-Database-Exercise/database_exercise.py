#!./venv/bin/python

"""

CRUD 

Create a program that displays the following menu:

1. Display database
2. Add an item
3. Delete an item
4. Change an item
5. Quit

The program contains a list of items; for example, fruits.

If you select 1, the program displays the items in the list, numbering each item. For example:

0: orange
1: banana
2: blackberry

If you select 2 the program asks you to enter a new item. It adds what you've typed to the list.

If you select 3, the program asks you to enter the list number of an item to delete. It deletes the specified item from the list.

If you select 4,  the program asks you to enter the list number of an item to change, then asks you to enter text. It changes the specified item to the speicified text. 

If you select 5, the program quits.

Until you quit with option 5, the program displays the menu again after every action.

"""
def main():
    pass
class Database:
    def __init__(self,list_of_strings):
        self.data = list_of_strings
    def display_data(self):
        for index, value in enumerate(self.data):
            print(f"{index}: {value}")
    def add_item(self):
        self.data.append(input("enter the new item: "))
    def delete_item(self):
        target_index = int(input("enter the index of the item to delete: "))
        if target_index < 0 or target_index > len(self.data) -1:
            print("invalid index, nothing's been deleted")
            return
        del self.data[target_index]
    def change_item(self):
        target_index = int(input("enter the index of the item to be replaced: "))
        if target_index < 0 or target_index > len(self.data) -1:
            print("invalid index, nothing's been deleted")
            return
        new_value = input("enter the new value for the item: ")
        self.data[target_index] = new_value
    def run_database(self):
        app_is_running = True
        menu = {
            "Display database": lambda: self.display_data(),
            "Add an item": lambda: self.add_item(),
            "Delete an item": lambda: self.delete_item(),
            "Change an item": lambda: self.change_item(),
            "Quit": lambda: app_is_running = False,
        }
        while app_is_runnin:
            
main()