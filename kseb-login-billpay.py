from selenium import webdriver

browser = webdriver.Firefox(executable_path="///home/shihas/Downloads/geckodriver-v0.27.0-linux64/geckodriver")

browser.get("https://wss.kseb.in/selfservices/wssloginUser.do")