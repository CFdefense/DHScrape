import json
import os
'''
    Function to parse json of user info and return user smtp addresses
'''
def parse_user_info() -> dict[str, str]:
    carrier_path: str = "user_data/carrier_ext.json"
    user_info_path: str = "user_data/user_info.json"
    user_addresses: dict[str, str] = {}

    # get saved user data
    with open(user_info_path, 'r') as file:
        user_json = json.load(file)

    # get saved carrier info
    with open(carrier_path, 'r') as file:
        carrier_json = json.load(file)

    # get relevant columns
    users = user_json['NUMBERS']
    carriers = carrier_json['CARRIERS']

    # for every name dict object create the email with carrier address
    for name, info in users.items():
        if info['carrier'] in carriers:
            user_addresses[name] = info['number'] + carriers[info['carrier']]
    
    return user_addresses