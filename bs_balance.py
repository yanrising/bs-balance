import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# User settings

LOGIN = ''
PIN = ''


# Main program

if __name__ == '__main__':
    # Start browser using Firefox webdriver.
    browser = webdriver.Firefox()
    # Load page with the login form.
    browser.get('https://www.berliner-sparkasse.de/')
    # Wait 2 seconds for all elements to load
    time.sleep(2)
    # Find login form by xpath and save it to variable
    login_form = browser.find_element_by_xpath("//form[1]")
    # Input login from user settings
    login_form.send_keys(LOGIN)
    # Press TAB to switch to PIN input
    login_form.send_keys(Keys.TAB)
    # Input PIN from user settings
    login_form.send_keys(PIN)
    # Press Enter to submit form
    login_form.send_keys(Keys.ENTER)
    # Wait 2 seconds for all elements to load
    time.sleep(2)
    # Find td element containing account balance
    balance_elem = browser.find_element_by_xpath('//table/tbody/tr[3]/td[2]')
    # Extract text value from found element
    balance = balance_elem.text
    # Close browser window
    browser.close()
    # Print result to console
    print('\nBalance:', balance, 'EUR\n')
