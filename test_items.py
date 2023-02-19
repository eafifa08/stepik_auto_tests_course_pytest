import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

class TestSite:
    def test_is_basket_button_exist(self, browser):
        browser.get(link)
        time.sleep(3)
        el_button_basket = browser.find_elements(By.CLASS_NAME,'btn-add-to-basket')
        print(f'button text={el_button_basket[0].text}')
        assert len(el_button_basket) > 0, 'Button "add to basket" is not exist'
    