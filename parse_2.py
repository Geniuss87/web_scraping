# from selenium import webdriver
# from time import sleep
# from random import choice
# from selenium.webdriver.common.by import By
#
# phones = ['4951553668', '4950818500', '4954298904']
# PATH = "//home/user/bin/chromedriver/chromedriver"
# driver = webdriver.Chrome(PATH)
#
# url = 'http://bosch.kofemashini.com/'
# driver.get(url)
#
# element = driver.find_element(By.TAG_NAME, "Input")
# element.click()
# element.send_keys(choice(phones))
# sleep(15)


# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from time import sleep
#
# PATH = "/home/user/bin/chromedriver/chromedriver"
# S = Service(PATH)
# driver = webdriver.Chrome(service=S)
#
# driver.get("https://www.accuweather.com/ru/browse-locations/asi/kg")
#
#
# driver.find_element(By.TAG_NAME, "Input").send_keys("Каракол, Иссык-Куль")
#
#
# driver.find_element(By.CLASS_NAME, "icon-search").click()
# sleep(15)


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

marka = input("Vvedite marku ")
model = input("Vvedite model ")

PATH = "/home/user/bin/chromedriver/chromedriver"
S = Service(PATH)
driver = webdriver.Chrome(service=S)


driver.get("https://cars.kg/")

find_marka = \
    driver.find_element(By.NAME, "vendor")
select_marka = Select(find_marka)
select_marka.select_by_visible_text("  " + marka)

select_model = Select(driver.find_element(By.NAME, "model"))
sleep(1)
select_model.select_by_visible_text("  " + model)

driver.find_element(By.TAG_NAME, "Button").click()
sleep(5)


html = driver.page_source
soup = BeautifulSoup(html)

