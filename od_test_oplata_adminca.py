from datetime import datetime
import pytest
from selenium import webdriver
import time
import re
import os

# -----------------------------------------Screen size--------------------------------------------------------------
# Регистрация переход на пеймент оплата проверка Platinum
# -----------------------------------------Screen size--------------------------------------------------------------
browser = webdriver.Chrome()
browser.maximize_window()
link = 'https://www.onlinedivorce.com'
browser.get(link)
browser.implicitly_Wait(10)

email = f'leonid+{"".join(i for i in datetime.now().isoformat() if i.isdigit())}@onlinedivorce.com'
states = ['//*[@id="id_state_of_filing"]/option[3]', '//*[@id="id_state_of_filing"]/option[3]'],

browser.find_element_by_xpath('//*[@id="id_state_of_filing"]').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="id_state_of_filing"]/option[6]').click()
browser.find_element_by_xpath('//*[@id="id_first_name"]').send_keys('first_na')
browser.find_element_by_xpath('//*[@id="id_last_name"]').send_keys('last_na')
browser.find_element_by_xpath('//*[@id="id_email"]').send_keys(email)

state_main_page = browser.find_element_by_xpath('//*[@id="id_state_of_filing"]/option[6]').get_attribute("value")
state_main_page = state_main_page.title()
first_name_main_page = browser.find_element_by_xpath('//*[@id="id_first_name"]').get_attribute("value")
last_name_main_page = browser.find_element_by_xpath('//*[@id="id_last_name"]').get_attribute("value")
email_main_page = email
browser.find_element_by_xpath('//*[@id="begin"]/div[7]/div/input').click()

# Step 2
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/div/div/button').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/div/div/div/ul/li[5]/a/span[1]').click()
browser.find_element_by_xpath('//*[@id="id_date_of_marriage_1"]').send_keys('12')
browser.find_element_by_xpath('//*[@id="id_date_of_marriage_2"]').send_keys('1999')
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()

# Step 3
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/button/span[1]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/div/ul/li[4]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[2]/div[3]/div/button/span[1]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[2]/div[3]/div/div/ul/li[3]/a').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()

# Step 4

browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/button/span[1]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/div/ul/li[2]/a').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[2]/div[3]/div/button/span[1]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[2]/div[3]/div/div/ul/li[3]/a').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()


# Step 5

browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div/div[3]/div/button/span[1]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div/div[3]/div/div/ul/li[3]/a/span[1]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()


# Step 6

browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/button/span[1]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/div/ul/li[2]/a/span[1]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()


# Step 7

browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div/div[3]/div/button/span[1]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div/div[3]/div/div/ul/li[3]/a/span[1]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()


# Step 8

browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div/div[3]/div/button/span[1]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div/div[3]/div/div/ul/li[3]/a/span[1]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()


# Step 9

browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/button').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/div/ul/li[3]/a/span[1]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[2]/div[3]/div/button/span[1]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[2]/div[3]/div/div/ul/li[3]/a/span[1]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()


# Step 10

browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/button/span[1]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/div/ul/li[2]/a/span[1]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[2]/div[3]/div/button/span[1]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[2]/div[3]/div/div/ul/li[3]/a/span[1]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()


# Step 11

browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div/div[3]/div/button/span[1]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div/div[3]/div/div/ul/li[3]/a/span[1]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()


# Step 12

browser.find_element_by_xpath('//*[@id="id_password"]').send_keys('11111')
# Сделать проверку введенных значений
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div[1]/div[2]/input').click()

# Pop up number fone

browser.find_element_by_xpath('//*[@id="number1"]').send_keys('111')
browser.find_element_by_xpath('//*[@id="number2"]').send_keys('111')
time.sleep(1)
browser.find_element_by_xpath('//*[@id="number3"]').send_keys('1112')


fone_1 = browser.find_element_by_xpath('//*[@id="number1"]').get_attribute("value")
fone_2 = browser.find_element_by_xpath('//*[@id="number2"]').get_attribute("value")
fone_3 = browser.find_element_by_xpath('//*[@id="number3"]').get_attribute("value")


browser.find_element_by_xpath('//*[@id="save-phone-js"]').click()
time.sleep(3)


coupone_url = browser.current_url
new_params = ('?coupon=gregrublev13899')
browser.get(coupone_url + new_params)

    # Paymant

browser.find_element_by_xpath('//*[@id="id_ccexp_m"]').click()
browser.find_element_by_xpath('//*[@id="id_ccexp_m"]/option[2]').click()

browser.find_element_by_xpath('//*[@id="id_ccexp_y"]').click()
browser.find_element_by_xpath('//*[@id="id_ccexp_y"]/option[11]').click()

browser.find_element_by_xpath('//*[@id="id_ccnum"]').send_keys('4731 1856 1731 8578	')

browser.find_element_by_xpath('//*[@id="id_addr1"]').send_keys('Adress1')
browser.find_element_by_xpath('//*[@id="id_city"]').send_keys('City')
browser.find_element_by_xpath('//*[@id="id_zip"]').send_keys('111')
browser.implicitly_Wait(10)
browser.find_element_by_xpath('//*[@id="payment-form"]/div/div[5]/div[2]/div[1]/button').click()
browser.implicitly_Wait(10)

#Buying Platinum
# browser.find_element_by_xpath('/html/body/div[1]/div[1]/main/div[1]/div/div[2]/div[5]/button').click()
# time.sleep(2)
# browser.find_element_by_xpath('//*[@id="event-purchase-content"]/div/div/div/div[3]/a').click()
# time.sleep(2)
# browser.find_element_by_xpath('//*[@id="platinumLocation"]/div/div/div[2]/div/div/div[2]/label[1]/span[2]').click()
# browser.find_element_by_xpath('//*[@id="platinumLocation"]/div/div/div[2]/div/div/div[3]/label[1]/span[2]').click()
# browser.find_element_by_xpath('//*[@id="platinumLocation"]/div/div/div[2]/div/div/div[5]/a').click()

#Skip Platinum
browser.find_element_by_xpath('/html/body/div[1]/div[1]/main/div[3]/div/div/div/small/a').click()
browser.implicitly_Wait(10)

experement_platinum = browser.find_element_by_class_name('guarantee-h2')
# if experement_platinum = :
#     browser.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div[1]/form/div/div/fieldset/div[1]/div[2]/div[1]/button/span[1]').click()
#     browser.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div[1]/form/div/div/fieldset/div[1]/div[2]/div[1]/div/ul/li[2]/a').click()
#     browser.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div[1]/form/div/div/fieldset/div[2]/div[2]/div[1]/button/span[1]').click()
#     browser.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div[1]/form/div/div/fieldset/div[2]/div[2]/div[1]/div/ul/li[2]/a').click()
#     browser.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div[1]/form/div/div/fieldset/div[3]/input').click()
#     # Skip Buying WILL
#     browser.find_element_by_xpath('//*[@id="willModalStep1"]/button/span/i').click()
# else:
    #Skip Buying WILL
    browser.find_element_by_xpath('//*[@id="willModalStep1"]/button/span/i').click()
    brow
#Buying WILL
#browser.find_element_by_xpath('//*[@id="willModalStep1"]/div[6]/div[2]/button').click()

browser.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div/div[2]/a[1]').click()
browser.find_element_by_xpath('//*[@id="welcomeModal"]/div/div/div[1]/button/span').click()

browser.find_element_by_xpath('//*[@id="nav"]/li[2]/a').click()

#Voronka
browser.find_element_by_xpath('//*[@id="id_husband_or_wife"]').click()
browser.find_element_by_xpath('//*[@id="id_husband_or_wife"]/option[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

browser.quit()

#_______________________________________Adminca___________________________________________________


browser = webdriver.Chrome()
browser.maximize_window()
link = 'https://www.completecase.com/admin/login/?next=/admin/'
browser.get(link)
browser.implicitly_Wait(10)


browser.find_element_by_xpath('//*[@id="id_username"]').send_keys('cmo0lkamd0jqflzrm49u6yin601kc1wn')
browser.find_element_by_xpath('//*[@id="id_password"]').send_keys('11111')
browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()

browser.find_element_by_xpath('//*[@id="search"]').send_keys(email)
browser.find_element_by_xpath('//*[@id="submit"]').click()

browser.find_element_by_xpath('//*[@id="result_list"]/tbody/tr/th/a').click()


first_name = browser.find_element_by_xpath('//*[@id="id_first_name"]').get_attribute("value")
last_name = browser.find_element_by_xpath('//*[@id="id_last_name"]').get_attribute("value")
number_fone = browser.find_element_by_xpath('//*[@id="id_phone"]').get_attribute("value")
state = browser.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[5]/div[2]/div[1]/div').get_attribute("value")
fone_main = fone_1 + fone_2 + fone_3

assert state == state_main_page, f"Hera se: {state}, a dolzhen bít: {state_main_page}"
assert first_name_main_page == first_name, f"Pokazyvayet: {first_name}, a dolzhen bít: {first_name_main_page}"
assert last_name_main_page == last_name, f"Pokazyvayet: {last_name}, a dolzhen bít: {last_name_main_page}"
assert fone_main == number_fone, f"Pokazyvayet: {number_fone}, a dolzhen bít: {fone_main}"

browser.quit()
