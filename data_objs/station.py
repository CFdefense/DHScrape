from .item import Item

'''
    Class for Stations
'''
class Station:

    def __init__(self, new_name:str):
        self.my_name: str = new_name
        self.my_items: list[Item] = []

    def __repr__(self):
        print(f"Station Name: {self.my_name} and Station Cals: {self.my_items}")