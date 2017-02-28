import getpass
import time
import sys

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

date = raw_input("date [yyyy-mm-dd]: ")
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

# Searches for available rooms
# date_field = driver.find_element_by_xpath("""//*[@id="leftresdate"]""")
# start_select = Select(driver.find_element_by_xpath(
#     """//*[@id="contents"]/div[2]/table/tbody/tr/td[3]/div/select[1]"""
# ))
# end_select = Select(driver.find_element_by_xpath(
#     """//*[@id="contents"]/div[2]/table/tbody/tr/td[4]/div/select[1]"""
# ))
# building_button = driver.find_element_by_xpath(
#     """//*[@id="ffsetx195"]/div/table/tbody/tr[2]/td[2]/button"""
# )
# building_a = driver.find_element_by_xpath("""//*[@id="ui-multiselect-ff195x_26-option-1"]""")
# building_select = Select(driver.find_element_by_xpath("""//*[@id="ff195x_26"]"""))
# driver.find_element_by_xpath(
#     """//*[@id="contents"]/div[2]/table/tbody/tr/td[2]/label"""
# ).click()


# date_field.clear()
# date_field.send_keys(date)
# start_select.select_by_visible_text(start_time)
# end_select.select_by_visible_text(end_time)
# ActionChains(driver).move_to_element(
#     building_button).click().perform()
# # building_button.click()
# # building_select.select_by_visible_text("A-huset")
# # building_select.select_by_visible_text("B-huset")
# sys.exit()
# room_field = driver.find_element_by_xpath(
#     """//*[@id="ffsetx195"]/div/table/tbody/tr[1]/td[2]/input[1]"""
# )
# room_field.send_keys(room)
# time.sleep(2)

# Finds the first available room and clicks on that room
room_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((
    By.XPATH, """//*[@id="objectselectionresult"]/table/tbody/tr[2]"""
)))
room_element.click()

# Activates time selection (change the second div for different days)
# 1 is today, 3 is in two days
hour_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((
    By.XPATH, """//*[@id="objectselectionresult"]/table/tbody/\
    tr[3]/td/div[1]/div[3]/div[3]/div[2]/div[1]"""
)))

driver.find_element_by_xpath(
    """//*[@id="objectselectionresult"]/table/tbody/\
    tr[3]/td/div[1]/div[3]/div[3]/div[2]/div[1]"""
)
hidden_element = driver.find_element_by_xpath(
    """//*[@id="newResDiv"]"""
)
ActionChains(driver).move_to_element(
    hour_element).click(hidden_element).perform()

# Selects a time slot
driver.find_element_by_xpath(
    """//*[@id="newResTimeDiv"]/tbody/tr/td[3]/input"""
).click()

# Inputs the wanted start and end times
date_field_submit = driver.find_element_by_xpath(
    """//*[@id="leftresdatepresent"]""")
start_select_submit = Select(driver.find_element_by_xpath(
    """//*[@id="reserveformedit"]/div[1]/select[1]"""
))
end_select_submit = Select(driver.find_element_by_xpath(
    """//*[@id="reserveformedit"]/div[1]/select[3]"""
))
building_list_button = driver.find_element_by_xpath(
    """//*[@id="leftreswrap"]/div/table/tbody/tr[1]/td/span"""
)
category_button = driver.find_element_by_xpath(
    """//*[@id="searchDivContent2"]/div[2]/h2[2]/div/a"""
)
date_field_submit.clear()
date_field_submit.send_keys(date)
start_select_submit.select_by_visible_text(start_time)
end_select_submit.select_by_visible_text(end_time)
building_list_button.click()
# TODO cant find and click on the button
# ActionChains(driver).move_to_element(building_list_button).click(building_list_button).\
    # move_to_element(category_button).click(category_button).perform()

# Clicks the book button!
# driver.find_element_by_xpath("""//*[@id="continueRes2"]""").click()
# driver.find_element_by_xpath("""//*[@id="showsendmail"]""").click()
print("Done! A confirmation email has been sent.")
