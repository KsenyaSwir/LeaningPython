from selenium import webdriver
from selenium.webdriver.support.select import Select


browser = webdriver.Chrome()

browser.get('https://techstepacademy.com/training-ground')

sel = browser.find_element_by_id('sel1')
my_select = Select(sel)
my_select.select_by_visible_text('Beets')