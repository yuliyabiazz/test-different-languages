import pytest
import time
from selenium import webdriver


def test_if_basket_button_exists(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_css_selector("[type = 'submit']") 
        
    assert button is not None, "Basket button doesn't exist."

