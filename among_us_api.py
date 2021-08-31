# import bot settings
from setting import *

# function to find the update using selenium
def webScrape():
    # the three lines below don't work at the moment, will be fixed; it is meant to open webdriver without opening the window
    options = Options()
    options.use_chromium = True
    options.add_argument("headless")
    # use whichever one, i used edge driver just because the developers of edge (Microsoft)
    # had official webdrivers
    driver = webdriver.Edge('./edgedriver' )
    # driver = webdriver.Crhome('./chromedriver')
    driver.get("https://innersloth.itch.io/among-us/devlog")
    # lets the website load
    driver.implicitly_wait(100)
    # looks for the last checked date
    message = driver.find_element_by_xpath("//abbr[@title=last_confirmed_date]")
    # stops the webdriver
    driver.close()
    return message

# used for debugging purposes
webScrape()

# schedules the function to run every hour
schedule.every().hour.do(webScrape)
