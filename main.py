from tools.scrape import getMenu
from data_objs.meal import Meal
from tools.notify import send_notification
from tools.parse_info import parse_user_info

'''
    Verbose Outputting Function
'''
def verbose(msg: str):
    print(f"SCRAPER VERBOSE: {msg}")

'''
    Scraper Main Function
'''
def main():
    # Get Previous Responses (IMAP)



    # Update Profiles and AI



    # Scrape Data
    verbose("SCRAPING API DATA")
    scraped_meals: list[Meal] = getMenu()

    # Check Scraped Data Validity
    if len(scraped_meals) == 0:
        verbose("ERROR: API SCRAPE FAILED")
        exit
    else:
        verbose("API SCRAPE - SUCCESSFUL")

    # Get Saved User Info
    verbose("GETTING USER DATA")
    user_data: dict[str, str] = parse_user_info() 

    # Check User Info Validity
    if not user_data:
        verbose("ERROR: NO SAVED USER DATA")
        exit
    else:
        verbose("USER DATA - VALIDATED")



    # Format Notification



    # AI Analysis



    # Send Notification
    '''
    verbose("SENDING NOTIFICATIONS")
    result: bool = send_notification(scraped_meals, user_data)

    # Check Notification Validity
    if result == True:
        verbose("NOTIFICATION(S) SUCCESSFULLY SENT")
    else:
        verbose("NOTIFICATION(S) FAILED TO SEND")
    '''
if __name__ == "__main__":
    main()