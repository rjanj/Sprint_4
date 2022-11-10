import allure
from pages.main_page import MainPageScooter


class TestQuestions:

    @allure.description(
        'Проверяем, что при нажатии на первый вопрос появляется нужный ответ')
    def test_first_question(self, driver):
        question_one = MainPageScooter(driver)
        question_one.navigate_cookie_scroll()
        question_one_text = question_one.click_question_one_and_take_answer()
        assert question_one_text == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.description(
        'Проверяем, что при нажатии на второй вопрос появляется нужный ответ')
    def test_second_question(self, driver):
        question_two = MainPageScooter(driver)
        question_two.navigate_cookie_scroll()
        question_two_text = question_two.click_question_two_and_take_answer()
        assert question_two_text == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с ' \
                                    'друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.description(
        'Проверяем, что при нажатии на третий вопрос появляется нужный ответ')
    def test_third_question(self, driver):
        question_three = MainPageScooter(driver)
        question_three.navigate_cookie_scroll()
        question_three_text = question_three.click_question_three_and_take_answer()
        assert question_three_text == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение ' \
                                      'дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ ' \
                                      'курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 ' \
                                      'мая в 20:30.'

    @allure.description(
        'Проверяем, что при нажатии на четвертый вопрос появляется нужный ответ')
    def test_fourth_question(self, driver):
        question_four = MainPageScooter(driver)
        question_four.navigate_cookie_scroll()
        question_four_text = question_four.click_question_four_and_take_answer()
        assert question_four_text == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.description(
        'Проверяем, что при нажатии на пятый вопрос появляется нужный ответ')
    def test_fifth_question(self, driver):
        question_five = MainPageScooter(driver)
        question_five.navigate_cookie_scroll()
        question_five_text = question_five.click_question_five_and_take_answer()
        assert question_five_text == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по ' \
                                     'красивому номеру 1010.'

    @allure.description(
        'Проверяем, что при нажатии на шестой вопрос появляется нужный ответ')
    def test_sixth_question(self, driver):
        question_six = MainPageScooter(driver)
        question_six.navigate_cookie_scroll()
        question_six_text = question_six.click_question_six_and_take_answer()
        assert question_six_text == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже ' \
                                    'если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.description(
        'Проверяем, что при нажатии на седьмой вопрос появляется нужный ответ')
    def test_seventh_question(self, driver):
        question_seven = MainPageScooter(driver)
        question_seven.navigate_cookie_scroll()
        question_seven_text = question_seven.click_question_seven_and_take_answer()
        assert question_seven_text == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не " \
                                      "попросим. Все же свои."

    @allure.description(
        'Проверяем, что при нажатии на восьмой вопрос появляется нужный ответ')
    def test_eight_question(self, driver):
        question_eight = MainPageScooter(driver)
        question_eight.navigate_cookie_scroll()
        question_eight_text = question_eight.click_question_eight_and_take_answer()
        assert question_eight_text == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
