import time
from selenium.webdriver.common.by import By


def test_button_add_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    assert browser.find_element(
        By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
