import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.ui import Select

class Blog_ATS():
      name = "groyce"
      pwd = "instructor1a"
      address = "dodge street"
      city = "omaha"
      state = "nebraska"
      zip = "68106"
      email = "groyce@yahoo.com"
      phone = "4025671234"
      role = "Teacher"
      driver = webdriver.Chrome()
      driver.maximize_window()
      driver.get("http://schoolomaha.herokuapp.com/register/")
      elem = driver.find_element_by_id("id_name")
      elem.send_keys(name)
      elem = driver.find_element_by_id("id_password")
      elem.send_keys(pwd)
      elem = driver.find_element_by_id("id_address")
      elem.send_keys(address)
      elem = driver.find_element_by_id("id_city")
      elem.send_keys(city)
      elem = driver.find_element_by_id("id_state")
      elem.send_keys(state)
      elem = driver.find_element_by_id("id_zipcode")
      elem.send_keys(zip)
      elem = driver.find_element_by_id("id_email")
      elem.send_keys(email)
      elem = driver.find_element_by_id("id_cell_phone")
      elem.send_keys(phone)
     # dropDown = wait.until(expected_conditions.visibility_of_element_located((By.ID, 'id_role')))
      select = Select(driver.find_element_by_id('id_role'))
      #select = Select(dropDown)
      select.select_by_value('Teacher')
      time.sleep(5)
      elem = driver.find_element_by_xpath("/html/body/div/div/form/button").click()
      elem.send_keys(Keys.RETURN)
      driver.get("http://schoolomaha.herokuapp.com/")
      driver.close
      assert "Success"