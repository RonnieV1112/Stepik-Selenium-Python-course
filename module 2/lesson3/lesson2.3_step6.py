from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')

browser.find_element_by_css_selector('[type="submit"]').click()

# получаем новую вкладку
new_tab = browser.window_handles[1]

# переключаемся на полученную вкладку
browser.switch_to.window(new_tab)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x = browser.find_element_by_id('input_value').text
browser.find_element_by_id('answer').send_keys(calc(x))

browser.find_element_by_css_selector('[type="submit"]').click()
