import getpass
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

date = "2017-02-28"  # raw_input("date [yyyy-mm-dd]: ")
start_time = raw_input("Start time [hh]: ")
end_time = raw_input("End time [hh]: ")
room = raw_input("Room (Enter for AG32): ") or "AG32"
username = raw_input("liu-id: ")
password = getpass.getpass(prompt="password: ")

# Navigates to LiU Time Edit and clicks on the login button
driver = webdriver.Chrome()
driver.get("https://se.timeedit.net/web/liu/db1/wr_stud/")
driver.find_element_by_xpath("""//*[@id="logincontrol"]/a[1]""").click()

# Fills in the login form and submits
username_field = driver.find_element_by_xpath("""//*[@id="username"]""")
password_field = driver.find_element_by_xpath("""//*[@id="password"]""")
username_field.send_keys(username)
password_field.send_keys(password)
driver.find_element_by_xpath(
    """//*[@id="login-box"]/div[6]/input[4]"""
).submit()

# Finds the button for Student Booking
driver.find_element_by_xpath(
    """//*[@id="contents"]/div[3]/div/div/a[1]"""
).click()
date_field = driver.find_element_by_xpath("""//*[@id="leftresdate"]""")
room_field = driver.find_element_by_xpath(
    """//*[@id="ffsetx195"]/div/table/tbody/tr[1]/td[2]/input[1]"""
)
date_field.clear()
date_field.send_keys(date)
room_field.send_keys(room)
time.sleep(2)

# Finds the first available room and clicks on that room
driver.find_element_by_xpath(
    """//*[@id="objectselectionresult"]/table/tbody/tr[2]""").click()
time.sleep(2)

# Activates time selection (change the second div for different days)
# 1 is today, 3 is in two days
driver.find_element_by_xpath(
    """//*[@id="objectselectionresult"]/\
    table/tbody/tr[3]/td/div[1]/div[3]/div[3]/div[3]"""
).click()

# Inputs the start and end time of the booking and reserves the time spot
start_select = Select(driver.find_element_by_xpath(
    """//*[@id="newResTimeDiv"]/tbody/tr/td[1]/select[1]"""
))
end_select = Select(driver.find_element_by_xpath(
    """//*[@id="newResTimeDiv"]/tbody/tr/td[2]/select[1]"""
))
start_select.select_by_visible_text(start_time)
end_select.select_by_visible_text(end_time)
driver.find_element_by_xpath(
    """//*[@id="newResTimeDiv"]/tbody/tr/td[3]/input"""
).click()

# Clicks the book button!
driver.find_element_by_xpath("""//*[@id="continueRes2"]""").click()
driver.find_element_by_xpath("""//*[@id="showsendmail"]""").click()
print("Done! A confirmation email has been sent.")
