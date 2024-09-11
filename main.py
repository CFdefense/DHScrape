from tools.scrape import getMenu
from data_objs.meal import Meal

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
    
    # try https://medium.com/testingonprod/how-to-send-text-messages-with-python-for-free-a7c92816e1a4


if __name__ == "__main__":
    main()