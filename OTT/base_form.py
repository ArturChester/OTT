from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def element_is_present(browser, by, value):
    try:
        browser.find_element(by, value)
        return True
    except NoSuchElementException:
        return False
