from selenium import webdriver
import time

browser = webdriver.Firefox(executable_path="///home/shihas/Downloads/geckodriver-v0.27.0-linux64/geckodriver")

browser.get("https://wss.kseb.in/selfservices/wssloginUser.do")

time.sleep(2)

user_name = browser.find_element_by_xpath('//*[@id="appendedtext1"]')
user_name.send_keys('username')

passWord = browser.find_element_by_xpath('//*[@id="appendedtext2"]')
passWord.send_keys('password')

sign_in = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/div[3]/button')
sign_in.click()

time.sleep(2)

proceed_pay = browser.find_element_by_xpath('//*[@id="registerForm"]/div[2]/div[3]/div/button')
proceed_pay.click()

debit_card = browser.find_element_by_xpath('//*[@id="pmOptions"]/button[3]')
debit_card.click()