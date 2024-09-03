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

        #todays food note is chicken tinga