import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Blog_ATS():
      driver = webdriver.Chrome()
      user = "kmangugari@unomaha.edu"
      pwd = "teacher"
      driver.maximize_window()
      driver.get("http://omschool.herokuapp.com/accounts/login")
      elem = driver.find_element_by_id("id_username")
      elem.send_keys(user)
      elem = driver.find_element_by_id("id_password")
      elem.send_keys(pwd)
      elem.send_keys(Keys.RETURN)
      time.sleep(5)
      assert "Logged In"
      driver.get("http://omschool.herokuapp.com/event")
      time.sleep(5)
      elem = driver.find_element_by_value("🔊 Play")
      driver.close()