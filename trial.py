from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://techstepacademy.com/trial-of-the-stones")

stone_input = browser.find_element_by_id('r1Input')
stone_button = browser.find_element_by_id('r1Btn')
stone_result = browser.find_element_by_css_selector('div#passwordBanner > h4')
secrets_input = browser.find_element_by_css_selector('input#r2Input')
secrets_button = browser.find_element_by_id('r2Butn')

richest_merchants_name = browser.find_element_by_xpath('//p[text() = "3000"]/../span')
merchants_input = browser.find_element_by_id('r3Input')
merchants_button = browser.find_element_by_id('r3Butn')

check_button = browser.find_element_by_id('checkButn')

stone_input.send_keys('rock')
stone_button.click()
password = stone_result.text

secrets_input.send_keys(password)
secrets_button.click()

name = richest_merchants_name.text
merchants_input.send_keys(name)
merchants_button.click()

check_button.click()