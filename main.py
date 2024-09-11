from tools.scrape import getMenu
from data_objs.meal import Meal
from tools.notify import sendNotification

'''
    Verbose Outputting Function
'''
def verbose(msg: str):
    print(f"SCRAPER VERBOSE: {msg}")

'''
    Scraper Main Function
'''
def main():
    # Scrape Data
    verbose("SCRAPING API DATA")
    scraped_meals: list[Meal] = getMenu('https://dineoncampus.com/marist')

    # Check Scraped Data Validity
    if len(scraped_meals) == 0:
        verbose("API SCRAPE FAILED")
        exit
    else:
        verbose("API SCRAPE SUCCESSFUL")

    # Send Notification
    verbose("SENDING NOTIFICATIONS")
    result: bool = sendNotification(scraped_meals)

    if result == True:
        verbose("NOTIFICATION SUCCESSFULLY SENT")
    else:
        verbose("NOTIFICATION FAILED")

if __name__ == "__main__":
    main()