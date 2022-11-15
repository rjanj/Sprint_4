from selenium.webdriver.common.by import By


class OrderPageLocators:
    name_field = (By.XPATH, '//input[@placeholder="* Имя"]')
    second_name_field = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    address_field = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    metro_station_field = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    metro_list = (By.XPATH, "//ul/li[@data-value='5' and @data-index='4']")
    telephone_field = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')

    next_button = (By.XPATH, "//button[text() = 'Далее']")

    delivery_time_field = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    calendar_field = (By.XPATH, "//div[@aria-label='Choose четверг, 10-е ноября 2022 г.']")

    period_field = (By.XPATH, "//div[text() ='* Срок аренды']")
    period_field_three_days = (By.XPATH, "//div[text() = 'трое суток']")

    scooter_color_black = (By.XPATH, "//label[text() = 'чёрный жемчуг']")

    note_field = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')

    order_button = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]')
    order_complete_button = (By.XPATH, "//button[2][text() = 'Да']")

    order_status_button = (By.XPATH, "//button[text() = 'Посмотреть статус']")
    order_complete_text = (By.XPATH, "//div[text() = 'Заказ оформлен']")

    main_order_button = (By.XPATH, '//button[@class="Button_Button__ra12g" and text() = "Заказать"]')
    main_order_button_two = (By.XPATH, '//button[text()="Заказать"]')

    scooter_image = (By.XPATH, "//img[@alt='Scooter']")
    yandex_image = (By.XPATH, "//img[@alt='Yandex']")
    cookies_accept = (By.XPATH, "//button[text() = 'да все привыкли']")
