link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

    # запуск - pytest -v --tb=line --locale=en  module_3/test_locale.py