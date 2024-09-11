'''
    Class for Items
'''
class Item:

    def __init__(self, new_name:str, new_cals:int):
        self.my_name = new_name
        self.my_cals = new_cals

    def __repr__(self):
        print(f"Item Name: {self.my_name} and Item Cals: {self.my_cals}")