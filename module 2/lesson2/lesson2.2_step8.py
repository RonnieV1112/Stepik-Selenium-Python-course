from selenium import webdriver
import os


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

browser.find_element_by_name('firstname').send_keys('firstName')
browser.find_element_by_name('lastname').send_keys('lastNAme')
browser.find_element_by_name('email').send_keys('email.ru')

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
browser.find_element_by_css_selector('[type="file"]').send_keys(file_path)

browser.find_element_by_css_selector('[type="submit"]').click()

