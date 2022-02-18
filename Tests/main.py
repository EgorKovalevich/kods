import time
from selenium import webdriver
from auth_data import password
from selenium.webdriver.common.keys import Keys
import random
import string

def main():
   driver = webdriver.Chrome()
   parser = Main(driver)
   parser.parse()

class Main(object):
   def __init__(self, driver):
      self.driver = driver

   def parse(self):
      self.register()
      self.topics()
      self.create_topics()
      self.create_new_topics()
      self.entry()
      self.exit()


   def register(self,):
      self.driver.get("http://localhost:8000/")
      button = self.driver.find_element_by_id("1234").click()
      time.sleep(1)

      login_input = self.driver.find_element_by_id("id_username")
      login_input.clear()
      login_input.send_keys(random.randint(1,9999999))
      time.sleep(1)

      password1 = self.driver.find_element_by_id("id_password1")
      password1.clear()
      password1.send_keys(password)
      time.sleep(1)

      password2 = self.driver.find_element_by_id("id_password2")
      password2.clear()
      password2.send_keys(password)
      time.sleep(1)

      password2.send_keys(Keys.ENTER)
      # button_reg = self.driver.find_element_by_id("1233").click()
      time.sleep(1)


   def topics(self):
      self.driver.get("http://localhost:8000/")
      button_topic = self.driver.find_element_by_id("1111").click()
      time.sleep(1)

   def create_topics(self):
      self.driver.get("http://localhost:8000/topics/")
      button_cr_topics = self.driver.find_element_by_id("1122").click()
      time.sleep(1)

   def create_new_topics(self):
      self.driver.get("http://localhost:8000/new_topic/")
      new_topics = self.driver.find_element_by_id("id_text")
      new_topics.clear()
      new_topics.send_keys(random.sample(string.ascii_lowercase,8))
      time.sleep(1)

      buttom_new_topic = self.driver.find_element_by_id("1123").click()
      time.sleep(1)

   def entry(self):
      self.driver.get("http://localhost:8000/topics/")
      buttom_ret = self.driver.find_element_by_id("1223")
      time.sleep(1)

      atr = buttom_ret.get_attribute("href")
      buttom_ret.click()
      time.sleep(1)

      argument = atr.split("/")[-2]
      self.driver.get("http://localhost:8000/topic/"+argument+"/")
      buttom_entry = self.driver.find_element_by_id("2333").click()
      time.sleep(1)

      self.driver.get("http://localhost:8000/new_entry/" + argument + "/")
      entry = self.driver.find_element_by_id("id_text")
      entry.clear()
      entry.send_keys(random.sample(string.ascii_lowercase,20))
      time.sleep(1)

      buttom_entry = self.driver.find_element_by_id("2233").click()
      time.sleep(1)

      self.driver.get("http://localhost:8000/topic/" + argument + "/")
      buttom_edit = self.driver.find_element_by_id("3333")
      atreb = buttom_edit.get_attribute("href")
      buttom_edit.click()
      time.sleep(1)

      argument1 = atreb.split("/")[-2]
      self.driver.get("http://localhost:8000/edit_entry/" + argument1 + "/")
      new_entry = self.driver.find_element_by_id("id_text")
      new_entry.clear()
      time.sleep(1)

      new_entry.send_keys(random.sample(string.ascii_lowercase, 10))
      time.sleep(1)

      buttom_edit_entry= self.driver.find_element_by_id("333").click()
      time.sleep(1)

      self.driver.get("http://localhost:8000/topic/" + argument + "/")
      buttom_edit_ret = self.driver.find_element_by_id("3333")
      buttom_edit_ret.click()
      time.sleep(1)

      self.driver.get("http://localhost:8000/edit_entry/" + argument1 + "/")
      buttom_del = self.driver.find_element_by_id("222")
      buttom_del.click()
      time.sleep(1)

      self.driver.get("http://localhost:8000/entry/" + argument1 + "/delete")
      delete_entry = self.driver.find_element_by_id("22").click()
      time.sleep(1)

      self.driver.get("http://localhost:8000/topic/" + argument + "/")
      delete = self.driver.find_element_by_id("33333").click()
      time.sleep(1)

      self.driver.get("http://localhost:8000/topic/" + argument + "/delete")
      delete_topic = self.driver.find_element_by_id("333333").click()
      time.sleep(1)

      self.driver.get("http://localhost:8000/topics/")
      button_learning = self.driver.find_element_by_id("1222").click()
      time.sleep(1)

   def exit(self):
      self.driver.get("http://localhost:8000/")
      exit = self.driver.find_element_by_id("11").click()
      time.sleep(5)

if __name__ == "__main__":
   main()






