from .station import Station

'''
    Class for Meals
'''
class Meal:

    def __init__(self, new_name: str):
        self.my_name: str = new_name
        self.my_stations: list[Station] = []

    def __repr__(self):
        print(f"Meal Name: {self.my_name} and Meal Cals: {self.my_stations}")