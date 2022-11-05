from selenium.webdriver.common.by import By


class MainPageLocators:  # Главная страница
    question_one_text = (By.ID, "accordion__heading-0")
    question_one_answer = (By.XPATH, "//p[text() = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.']")

    question_two_text = (By.ID, "accordion__heading-1")
    question_two_answer = (By.XPATH, "//p[text() = 'Пока что у нас так: один заказ — один самокат. Если хотите "
                                     "покататься с друзьями, можете просто сделать несколько заказов — один за "
                                     "другим.']")

    question_three_text = (By.ID, "accordion__heading-2")
    question_three_answer = (By.XPATH, "//p[text() = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 "
                                       "мая в течение дня. Отсчёт времени аренды начинается с момента, "
                                       "когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, "
                                       "суточная аренда закончится 9 мая в 20:30.']")

    question_four_text = (By.ID, "accordion__heading-3")
    question_four_answer = (By.XPATH, "//p[text() = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.']")

    question_five_text = (By.ID, "accordion__heading-4")
    question_five_answer = (By.XPATH, "//p[text() = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в "
                                      "поддержку по красивому номеру 1010.']")

    question_six_text = (By.ID, "accordion__heading-5")
    question_six_answer = (By.XPATH, "//p[text() = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на "
                                     "восемь суток — даже если будете кататься без передышек и во сне. Зарядка не "
                                     "понадобится.']")

    question_seven_text = (By.ID, "accordion__heading-6")
    question_seven_answer = (By.XPATH, "//p[text() = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной "
                                       "записки тоже не попросим. Все же свои.']")

    question_eight_text = (By.ID, "accordion__heading-7")
    question_eight_answer = (
        By.XPATH, "//p[text() = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']")

    cookies_accept = (By.XPATH, "//button[text() = 'да все привыкли']")

    scroll_to_questions = (By.XPATH, '//div[text()="Вопросы о важном"]')
