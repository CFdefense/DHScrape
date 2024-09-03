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

        pretty_json = json.dumps(json_data, indent=4, sort_keys=True)

        #print(pretty_json)

        #todays food note is chicken tinga