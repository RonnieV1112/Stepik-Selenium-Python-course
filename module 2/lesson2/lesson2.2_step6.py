from selenium import webdriver
import math

browser = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser.get("http://suninjuly.github.io/execute_script.html")

x = browser.find_element_by_id('input_value').text
browser.find_element_by_id('answer').send_keys(calc(x))

browser.find_element_by_id('robotCheckbox').click()
radio = browser.find_element_by_id('robotsRule')
browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
radio.click()

browser.find_element_by_css_selector('[type="submit"]').click()

