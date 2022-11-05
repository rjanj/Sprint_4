import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.order_page_locators import OrderPageLocators


class OrderPageScooter:
    name_field = OrderPageLocators.name_field
    second_name_field = OrderPageLocators.second_name_field
    address_field = OrderPageLocators.address_field
    metro_station_field = OrderPageLocators.metro_station_field
    metro_list = OrderPageLocators.metro_list
    telephone_field = OrderPageLocators.telephone_field
    next_button = OrderPageLocators.next_button
    delivery_time_field = OrderPageLocators.delivery_time_field
    calendar_field = OrderPageLocators.calendar_field
    period_field = OrderPageLocators.period_field
    period_field_three_days = OrderPageLocators.period_field_three_days
    scooter_color_black = OrderPageLocators.scooter_color_black
    note_field = OrderPageLocators.note_field
    order_button = OrderPageLocators.order_button
    order_complete_button = OrderPageLocators.order_complete_button
    order_complete_text = OrderPageLocators.order_complete_text
    order_status_button = OrderPageLocators.order_status_button
    main_order_button_one = OrderPageLocators.main_order_button
    main_order_button_two = OrderPageLocators.main_order_button_two
    scooter_image = OrderPageLocators.scooter_image
    yandex_image = OrderPageLocators.yandex_image
    cookies_accept = OrderPageLocators.cookies_accept

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем главную страницу Scooter')
    def navigate(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru')

    @allure.step('Нажали на кнопку "Заказать" в шапке сайта')
    def order_button_one_click(self):
        self.driver.find_element(*self.main_order_button_one).click()

    @allure.step('Нажали на кнопку заказать в теле сайта')
    def order_button_two_click(self):
        self.driver.find_element(*self.main_order_button_two).click()

    @allure.step('Вводим имя')
    def order_page_name_field(self, name):
        self.driver.find_element(*self.name_field).send_keys(name)

    @allure.step('Вводим фамилию')
    def order_page_second_name_field(self, second_name):
        self.driver.find_element(*self.second_name_field).send_keys(second_name)

    @allure.step('Вводим адрес')
    def order_page_address_field(self, adress):
        self.driver.find_element(*self.address_field).send_keys(adress)

    def order_page_metro_field_click(self):
        self.driver.find_element(*self.metro_station_field).click()

    @allure.step('Выбираем станцию метро')
    def order_page_metro_station_pick(self):
        self.driver.find_element(*self.metro_list).click()

    @allure.step('Вводим номер телефона')
    def order_page_telephone_number(self, number):
        self.driver.find_element(*self.telephone_field).send_keys(number)

    @allure.step('Жмем кнопку "Далее"')
    def order_page_button_next_click(self):
        self.driver.find_element(*self.next_button).click()

    def order_page_time_field_click(self):
        self.driver.find_element(*self.delivery_time_field).click()

    @allure.step('Выбираем дату доставки')
    def order_page_calendar_day_click(self):
        self.driver.find_element(*self.calendar_field).click()

    def order_page_period_field_click(self):
        self.driver.find_element(*self.period_field).click()

    @allure.step('Выбираем срок аренды')
    def order_page_period_three_days(self):
        self.driver.find_element(*self.period_field_three_days).click()

    @allure.step('Выбираем цвет самоката')
    def order_page_pick_black_scooter(self):
        self.driver.find_element(*self.scooter_color_black).click()

    @allure.step('Пишем комментарий курьеру')
    def order_page_courier_note_field(self, note):
        self.driver.find_element(*self.note_field).send_keys(note)

    @allure.step('Жмем кнопку "Заказать"')
    def order_page_order_button(self):
        self.driver.find_element(*self.order_button).click()

    @allure.step('Подтверждаем заказ')
    def order_page_order_complete_button(self):
        self.driver.find_element(*self.order_complete_button).click()

    def order_page_order_complete_text(self):
        order_complete_text = self.driver.find_element(*self.order_complete_text).text
        return order_complete_text

    @allure.step('Жмем кнопку "Посмотреть статус"')
    def order_page_status_button(self):
        self.driver.find_element(*self.order_status_button).click()

    @allure.step('Переход по клику на картинку "Самокат"')
    def scooter_image_click(self):
        self.driver.find_element(*self.scooter_image).click()

    @allure.step('Переход по клику на логотип "Яндекс"')
    def yandex_image_click(self):
        wait = WebDriverWait(self.driver, 10)
        original_window = self.driver.current_window_handle
        assert len(self.driver.window_handles) == 1
        self.driver.find_element(*self.yandex_image).click()
        wait.until(EC.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        wait.until(EC.title_is("Дзен"))

    def wait_element(self):
        WebDriverWait(self.driver, 5)
    def order_cookies_accept(self):
        self.driver.find_element(*self.cookies_accept).click()

    @allure.step('Заполнение полей заказа и его подтверждение')
    def order_page_login(self, name, second_name, address, number, note):
        self.order_page_name_field(name)
        self.order_page_second_name_field(second_name)
        self.order_page_address_field(address)
        self.order_page_metro_field_click()
        self.order_page_metro_station_pick()
        self.order_page_telephone_number(number)
        self.order_page_button_next_click()
        self.order_page_time_field_click()
        self.order_page_calendar_day_click()
        self.order_page_period_field_click()
        self.order_page_period_three_days()
        self.order_page_pick_black_scooter()
        self.order_page_courier_note_field(note)
        self.order_page_order_button()
        self.order_page_order_complete_button()
