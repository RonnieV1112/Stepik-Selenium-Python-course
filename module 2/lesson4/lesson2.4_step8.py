from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/explicit_wait2.html')

# ждем, пока цена не станет 100$
WebDriverWait(browser, 5).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
)
browser.find_element_by_id('book').click()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x = browser.find_element_by_id('input_value').text
browser.find_element_by_id('answer').send_keys(calc(x))

browser.find_element_by_css_selector('[type="submit"]').click()
