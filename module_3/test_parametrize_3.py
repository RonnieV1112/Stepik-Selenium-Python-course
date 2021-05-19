import math
import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize('link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_stepik_alien(browser, link):
    link = f"https://stepik.org/lesson/{link}/step/1"
    browser.get(link)

    answer = str(math.log(int(time.time())))

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))
    )
    browser.find_element_by_css_selector('textarea').send_keys(answer)
    browser.find_element_by_css_selector('.submit-submission').click()

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
    )

    actual_result = browser.find_element_by_css_selector('.smart-hints__hint').text
    expected_result = 'Correct!'
    print(actual_result)

    assert actual_result == expected_result, f'expected {expected_result}, got {actual_result}'