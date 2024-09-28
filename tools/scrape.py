import subprocess
import json
from datetime import datetime
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

    # Get the current date for the filename
    current_date = datetime.now().strftime('%Y-%m-%d')

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


                # create appropriate json object for each meal
                meal_document = {
                    "date": current_date,
                    "location": {
                        "id": location["id"],
                        "name": location["name"],
                        "type": location["type"],
                        "period": period["name"],
                        "stations": [
                            {
                                "id": station["id"],
                                "name": station["name"],
                                "items": station["items"]
                            } for station in period['stations']
                        ]
                    }
                }

                # store in its respective json
                file_name = f'json/menu/{period["name"]}.json'
                with open(file_name, 'w') as meal_file:
                    # Load existing data
                    existing_data = json.load(meal_file)
                    # Append new meal document to bottom of existing data
                    existing_data.append(meal_document)
                    # Move the file pointer to the beginning of the file
                    meal_file.seek(0)
                    # Save updated data back to the file
                    json.dump(existing_data, meal_file, indent=4)

                print(f"Updated {file_name} Contents")
                
    return my_meals