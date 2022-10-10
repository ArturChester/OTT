import time

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from base_form import element_is_present


def test_field_email_validation_error_1():
    """Проверка валидации при поле == NULL"""
    with Chrome() as browser:
        options = Options()
        options.add_argument('--headless')
        browser = webdriver.Chrome(options=options)
        browser.get("https://auth.instat.tv/authorize")
        browser.find_element(By.CSS_SELECTOR, '[placeholder="E-mail"]').send_keys()
        browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        assert element_is_present(browser, By.XPATH, '//span[text()="Enter your e-mail address"]'), 'Отсутствует валидация'

def test_field_email_validation_error_2():
    """Проверка валидации при поле != NULL"""
    with Chrome() as browser:
        options = Options()
        options.add_argument('--headless')
        browser = webdriver.Chrome(options=options)
        browser.get("https://auth.instat.tv/authorize")
        browser.find_element(By.CSS_SELECTOR, '[placeholder="E-mail"]').send_keys('test')
        browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        assert element_is_present(browser, By.XPATH, '//span[text()="Incorrect E-mail format"]'), 'Отсутствует валидация'

def test_field_email_validation_error_3():
    """Некорректный формат email"""
    with Chrome() as browser:
        options = Options()
        options.add_argument('--headless')
        browser = webdriver.Chrome(options=options)
        browser.get("https://auth.instat.tv/authorize")
        browser.find_element(By.CSS_SELECTOR, '[placeholder="E-mail"]').send_keys('artur.minnibaev@.com')
        browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        assert element_is_present(browser, By.XPATH,
                                  '//span[text()="Incorrect E-mail format"]'), 'Отсутствует валидация'

def test_field_email_validation_error_4():
    """Проверка валидации, если формат email введен верно, но остутствует пароль"""
    with Chrome() as browser:
        options = Options()
        options.add_argument('--headless')
        browser = webdriver.Chrome(options=options)
        browser.get("https://auth.instat.tv/authorize")
        browser.find_element(By.CSS_SELECTOR, '[placeholder="E-mail"]').send_keys('artur.minnibaev@instatsport.com')
        browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        assert element_is_present(browser, By.XPATH,
                                  '//span[text()="Enter your password"]'), 'Отсутствует валидация'
