import json
import os
'''
    Function to parse json of user info and return iterable dictionary
'''
def parse_user_info() -> dict[str, str]:
    carrier_path: str = "docs/carrier_ext.json"
    user_info_path: str = "docs/user_info.json"
    