import subprocess
import json
from datetime import datetime
from data_objs.meal import Meal
from data_objs.station import Station
from data_objs.item import Item

'''
    Method to Create Scrape And Populate Available Foods
'''
def getMenu() -> list[Meal]:
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

                # Store in its respective JSON file
                file_name = f'json/menu/{period["name"]}.json'

                # Open the existing JSON file
                try:
                    with open(file_name, 'r+') as meal_file:
                        # Load existing data
                        existing_data = json.load(meal_file)

                        # Check if the existing data is a list
                        if isinstance(existing_data, list):
                            existing_data.append(meal_document)  # Use append() to add the new meal document
                        else:
                            raise ValueError("Existing data is not in a list format.")

                        # Move the file pointer to the beginning of the file
                        meal_file.seek(0)
                        # Save updated data back to the file
                        json.dump(existing_data, meal_file, indent=4)
                        meal_file.truncate()  # Ensure no leftover data is retained

                except json.JSONDecodeError:
                    print(f"Error decoding JSON from {file_name}. Initializing new data.")
                    # Handle the case where JSON is invalid or empty
                    with open(file_name, 'w') as meal_file:
                        json.dump([meal_document], meal_file, indent=4)

                except ValueError as ve:
                    print(ve)
                    print("Initializing new data as a list.")
                    # If existing data is not a list, create a new list with the meal document
                    with open(file_name, 'w') as meal_file:
                        json.dump([meal_document], meal_file, indent=4)

                print(f"Added new meal to {file_name}")
                
    return my_meals