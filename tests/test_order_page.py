import time

import allure
from pages.order_page import OrderPageScooter


class TestScooterOrder:
    @allure.description(
        'Проверяем, что после заполнения данных и подтверждения заказа будет получено сообщение "Заказ оформлен"')
    def test_order_one(self, driver):
        reg_order = OrderPageScooter(driver)
        reg_order.navigate()
        reg_order.order_cookies_accept()
        reg_order.order_button_one_click()
        name = "Рома"
        second_name = "Роман"
        address = 'Зеленоград'
        number = '88005553535'
        note = 'Привет'
        reg_order.order_page_login(name, second_name, address, number, note)
        order_complete_text = reg_order.order_page_order_complete_text()
        assert 'Заказ оформлен' in order_complete_text

    @allure.description(
        'Проверяем, что после заполнения данных и подтверждения заказа будет получено сообщение "Заказ оформлен"')
    def test_order_two(self, driver):
        reg_order = OrderPageScooter(driver)
        reg_order.navigate()
        reg_order.order_cookies_accept()
        reg_order.order_button_two_click()
        name = "Антуан"
        second_name = "Антуанов"
        address = 'Истра'
        number = '88003333333'
        note = 'Мерси'
        reg_order.order_page_login(name, second_name, address, number, note)
        order_complete_text = reg_order.order_page_order_complete_text()
        assert 'Заказ оформлен' in order_complete_text


class TestSiteNavigating:
    @allure.description(
        'Проверяем, что после клика на логотип "Самокат" попадем на главную страницу')
    def test_rotating_scooter(self, driver):
        reg_order = OrderPageScooter(driver)
        reg_order.navigate()
        reg_order.order_cookies_accept()
        reg_order.order_button_two_click()
        name = "Жорик"
        second_name = "Сергеев"
        address = 'Москва'
        number = '88003333333'
        note = 'Спасибо'
        reg_order.order_page_login(name, second_name, address, number, note)
        reg_order.order_page_status_button()
        reg_order.scooter_image_click()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.description(
        'Проверяем, что после клика на логотип "Яндекс" попадем на главную страницу Dzen')
    def test_rotating_yandex(self, driver):
        reg_order = OrderPageScooter(driver)
        reg_order.navigate()
        reg_order.order_cookies_accept()
        reg_order.order_button_two_click()
        name = "Антон"
        second_name = "Астахов"
        address = 'Москва'
        number = '88003333333'
        note = 'Скорее бы'
        reg_order.order_page_login(name, second_name, address, number, note)
        reg_order.order_page_status_button()
        reg_order.yandex_image_click()
        assert driver.current_url == 'https://dzen.ru/?yredirect=true'
