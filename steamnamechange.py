from selenium import webdriver
import time
import colorama
import pyautogui
name = pyautogui.prompt("Enter Steam Name")
password = pyautogui.prompt("Enter Steam Password")
url = 'https://steamcommunity.com/login/home/?goto='
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(50)

driver.find_element_by_xpath("""//*[@id="steamAccountName"]""").send_keys(name)
driver.find_element_by_xpath("""//*[@id="steamPassword"]""").send_keys(password)
driver.find_element_by_xpath("""//*[@id="SteamLogin"]""").click()

pyautogui.alert('YOU HAVE 60 SECONDS TO GET YOUR CODE!')
time.sleep(60)
driver.find_element_by_xpath("""//*[@id="global_actions"]/a""").click()

driver.find_element_by_xpath("""/html/body/div[1]/div[7]/div[2]/div[1]/div[1]/div/div/div/div[3]/div[2]/a""").click()

while True:
	driver.find_element_by_xpath("""//*[@id="personaName"]""").clear()
	driver.find_element_by_xpath("""//*[@id="personaName"]""").send_keys("t")
	driver.find_element_by_xpath("""//*[@id="editForm"]/div[8]/div/button""").click()
	time.sleep(2.5)
	driver.find_element_by_xpath("""//*[@id="personaName"]""").clear()
	driver.find_element_by_xpath("""//*[@id="personaName"]""").send_keys("tu")
	driver.find_element_by_xpath("""//*[@id="editForm"]/div[8]/div/button""").click()
	time.sleep(2.5)
	driver.find_element_by_xpath("""//*[@id="personaName"]""").clear()
	driver.find_element_by_xpath("""//*[@id="personaName"]""").send_keys("tur")
	driver.find_element_by_xpath("""//*[@id="editForm"]/div[8]/div/button""").click()
	time.sleep(2.5)
	driver.find_element_by_xpath("""//*[@id="personaName"]""").clear()
	driver.find_element_by_xpath("""//*[@id="personaName"]""").send_keys("turt")
	driver.find_element_by_xpath("""//*[@id="editForm"]/div[8]/div/button""").click()
	time.sleep(2.5)
	driver.find_element_by_xpath("""//*[@id="personaName"]""").clear()
	driver.find_element_by_xpath("""//*[@id="personaName"]""").send_keys("turtl")
	driver.find_element_by_xpath("""//*[@id="editForm"]/div[8]/div/button""").click()
	time.sleep(15)

