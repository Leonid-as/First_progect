from selenium import webdriver


browser = webdriver.Chrome()
browser.maximize_window()
link = 'https://www.onlinedivorce.com'
browser.get(link)
