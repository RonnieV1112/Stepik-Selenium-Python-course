import time

from selenium.webdriver.support.ui import Select
from selenium import webdriver
import math

def calc(x, y):
  return str(int(x)+int(y))

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id('num1').text
    y = browser.find_element_by_id('num2').text

    res = calc(x, y)

    Select(browser.find_element_by_id('dropdown')).select_by_value(res)

    browser.find_element_by_css_selector('button[type="submit"]').click()

finally:
    time.sleep(30)
    browser.quit()
