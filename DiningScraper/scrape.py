import subprocess
import json
class Scraper:
    @staticmethod
    def getMenu(link):
        command = [
            'curl', 'https://api.dineoncampus.com/v1/sites/todays_menu?site_id=64b18f3bc625af0685e3c5eb'
        ]
        # Execute the 'ls -l' command and capture its output
        curl_request = subprocess.run(command, capture_output=True, text=True)

        # log as json
        json_data = json.loads(curl_request.stdout)

        for location in json_data['locations']:
            print(location['name'])
            if location['name'] == "Murray Dining Hall":
                for period in location['periods']:
                    print(period['name'])
                    if period['name'] == "Dinner":
                        for station in period['stations']:
                            print(station['name'])
                            for item in station['items']:
                                print(item['name'])

        #log all food in 3d arr of classes period -> station -> foods
        # try https://medium.com/testingonprod/how-to-send-text-messages-with-python-for-free-a7c92816e1a4
        # api link confirmed to stay updated 
