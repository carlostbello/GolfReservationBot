from selenium import webdriver
from numpy import loadtxt
import schedule
import time

browser = webdriver.Chrome('D:\Programming Projects\Project 1\chromedriver')
browser.get('http://staelenagolf.com/default.aspx')

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

schedule.every().monday.at('12:00').do(nextButtonP1.click())

# Date Path dependent on the given calendar date
dateButton = browser.find_element_by_xpath('//*[@id="MainContent_calendar"]/div/table/tbody/tr[3]/td[1]/a')
dateButton.click()

i = 4
stayLoop = True
timeButton = browser.find_elements_by_xpath('//*[@id="MainContent_c1_lvTeetimes_grpTemplate"]/li[' + str(i) + ']/a')
while stayLoop and i <= 3:
    timeButton = browser.find_elements_by_xpath('//*[@id="MainContent_c1_lvTeetimes_grpTemplate"]/li[' + str(i) + ']/a')
    if timeButton.get_attribute("title") == "Taken":
        i += 1
    else:
        stayLoop = False
timeButton.click()
