import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Blog_ATS():
      driver = webdriver.Chrome()
      user = "tejaswikandula@unomaha.edu"
      pwd = "student"
      driver.maximize_window()
      driver.get("http://omschool.herokuapp.com/accounts/login")
      elem = driver.find_element_by_id("id_username")
      elem.send_keys(user)
      elem = driver.find_element_by_id("id_password")
      elem.send_keys(pwd)
      elem.send_keys(Keys.RETURN)
      time.sleep(5)
      assert "Logged In"
      driver.get("http://omschool.herokuapp.com/student/slack/viewmsg")
      time.sleep(5)
      driver.get("http://omschool.herokuapp.com/student/home")
      time.sleep(5)
      driver.get("http://omschool.herokuapp.com/student/course/2/view/")
      time.sleep(5)
      driver.get("http://omschool.herokuapp.com/student/course/2/attendance/")
      time.sleep(5)      
      driver.get("http://omschool.herokuapp.com/student/course/2/schedule/")
      time.sleep(5)
      driver.get("http://omschool.herokuapp.com/student/course/2/syllabus/")
      time.sleep(5)
      driver.get("http://omschool.herokuapp.com/student/course/2/grades/")
      time.sleep(5)
      driver.get("http://omschool.herokuapp.com/student/course/2/exams/")
      time.sleep(5)
      driver.close()