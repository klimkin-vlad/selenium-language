from selenium.webdriver.common.by import By
import pytest
import time

link = f"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_buy_link(browser):
    browser.get(link)
    elements = browser.find_elements(By.CLASS_NAME, "add-to-basket")
    time.sleep(60)
    assert len(elements) >= 1, "Корзина не найдена"
    assert len(elements) <= 1, "Неверный селектор"
    assert elements[0].is_displayed(), "Кнопка не видна"
