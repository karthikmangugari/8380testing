import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Blog_ATS():
      driver = webdriver.Chrome()
      user = "pmadiraju@unomaha.edu"
      pwd = "parent"
      zipc = "68124"
      driver.maximize_window()
      driver.get("http://omschool.herokuapp.com/accounts/login")
      elem = driver.find_element_by_id("id_username")
      elem.send_keys(user)
      elem = driver.find_element_by_id("id_password")
      elem.send_keys(pwd)
      elem.send_keys(Keys.RETURN)
      time.sleep(5)
      assert "Logged In"
      driver.get("http://omschool.herokuapp.com/parent/profile/view")
      time.sleep(5)
      driver.get("http://omschool.herokuapp.com/parent/profile/edit/")
      time.sleep(5)
      elem = driver.find_element_by_name('zipcode').clear()
      time.sleep(5)
      elem = driver.find_element_by_name('zipcode')
      elem.send_keys(zipc)
      elem.send_keys(Keys.RETURN)
      time.sleep(5)
      driver.close()