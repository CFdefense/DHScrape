import subprocess
import json
from data_objs.meal import Meal
from data_objs.station import Station
from data_objs.item import Item

'''
    Method to Create Scrape And Populate Available Foods
'''
def getMenu(link: str) -> list[Meal]:
    command = ['curl', 'https://api.dineoncampus.com/v1/sites/todays_menu?site_id=64b18f3bc625af0685e3c5eb'] # os cmd to run
    my_meals: list[Meal] = [] # to hold our meal objs

    try:
        # Execute curl command to pull api data
        curl_request = subprocess.run(command, capture_output=True, text=True)

        # log as json
        json_data = json.loads(curl_request.stdout)

    except Exception:
        # return empty list as flag for error
        return my_meals

    # parse json, create objs and append accordingly
    for location in json_data['locations']:
        if location['name'] == "Murray Dining Hall":
            for period in location['periods']:
                current_meal = Meal(period)
                for station in period['stations']:
                    current_station = Station(station)
                    current_meal.my_stations.append(current_station)
                    for item in station['items']:
                        current_station.my_items.append(item)
                my_meals.append(current_meal)
    return my_meals