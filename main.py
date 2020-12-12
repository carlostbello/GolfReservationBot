from selenium import webdriver
from numpy import loadtxt
import schedule
import time

# Retrieve webdriver via Selenium
browser = webdriver.Chrome('D:\Programming Projects\Project 1\chromedriver')
browser.get('http://staelenagolf.com/default.aspx')

# Load in the info to be filled ex. FName, LName, Member ID, email, etc.
lines = loadtxt("Contents.txt", dtype='str')

nameBar = browser.find_element_by_id("MainContent_txtFirstName")
nameBar.send_keys(lines[0])

nameBar = browser.find_element_by_id("MainContent_txtLastName")
nameBar.send_keys(lines[1])

nameBar = browser.find_element_by_id("MainContent_txtMemberID")
nameBar.send_keys(lines[2])

nameBar = browser.find_element_by_id("MainContent_txtEmail")
nameBar.send_keys(lines[3])

nameBar = browser.find_element_by_id("MainContent_txtNumPlayers")
nameBar.send_keys(lines[4])

nameBar = browser.find_element_by_id("MainContent_txtNumCarts")
nameBar.send_keys(lines[5])

nextButtonP1 = browser.find_element_by_id("MainContent_btnNext")
# Time trigger, as it is first come first serve
schedule.every().monday.at('12:00').do(nextButtonP1.click())

# Date Path dependent on the given calendar date
dateRow = str(3)
dateColumn = str(1)
dateButton = browser.find_element_by_xpath('//*[@id="MainContent_calendar"]/div/table/tbody/tr[' + dateRow + ']/td[' + dateColumn + ']/a')
dateButton.click()

# Time Selector. Cycle between 4 time slots between 6:45 and 7:15 
i = 4 # i = 4 because the 4th time slot is 6:45
stayLoop = True
timeButton = browser.find_elements_by_xpath('//*[@id="MainContent_c1_lvTeetimes_grpTemplate"]/li[' + str(i) + ']/a')
while stayLoop and i <= 3: # The increments are by 15 mins
    timeButton = browser.find_elements_by_xpath('//*[@id="MainContent_c1_lvTeetimes_grpTemplate"]/li[' + str(i) + ']/a')
    if timeButton.get_attribute("title") == "Taken":
        i += 1
    else:
        stayLoop = False
timeButton.click()
