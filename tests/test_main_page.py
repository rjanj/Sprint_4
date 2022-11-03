import allure
from pages.main_page import MainPageScooter


class TestQuestions:

    @allure.description(
        'Проверяем, что при нажатии на первый вопрос появляется нужный ответ')
    def test_first_question(self, driver):
        question_one = MainPageScooter(driver)
        question_one.navigate()
        question_one.main_questions_text_rotation()
        question_one.click_question_one()
        question_one_text = question_one.text_question_answer_one()
        assert question_one_text == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.description(
        'Проверяем, что при нажатии на второй вопрос появляется нужный ответ')
    def test_second_question(self, driver):
        question_two = MainPageScooter(driver)
        question_two.navigate()
        question_two.main_questions_text_rotation()
        question_two.click_question_two()
        question_two_text = question_two.text_question_answer_two()
        assert question_two_text == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с ' \
                                    'друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.description(
        'Проверяем, что при нажатии на третий вопрос появляется нужный ответ')
    def test_third_question(self, driver):
        question_three = MainPageScooter(driver)
        question_three.navigate()
        question_three.main_questions_text_rotation()
        question_three.click_question_three()
        question_three_text = question_three.text_question_answer_three()
        assert question_three_text == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение ' \
                                      'дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ ' \
                                      'курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 ' \
                                      'мая в 20:30.'

    @allure.description(
        'Проверяем, что при нажатии на четвертый вопрос появляется нужный ответ')
    def test_fourth_question(self, driver):
        question_four = MainPageScooter(driver)
        question_four.navigate()
        question_four.main_questions_text_rotation()
        question_four.click_question_four()
        question_four_text = question_four.text_question_answer_four()
        assert question_four_text == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.description(
        'Проверяем, что при нажатии на пятый вопрос появляется нужный ответ')
    def test_fifth_question(self, driver):
        question_five = MainPageScooter(driver)
        question_five.navigate()
        question_five.main_questions_text_rotation()
        question_five.click_question_five()
        question_five_text = question_five.text_question_answer_five()
        assert question_five_text == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по ' \
                                     'красивому номеру 1010.'

    @allure.description(
        'Проверяем, что при нажатии на шестой вопрос появляется нужный ответ')
    def test_sixth_question(self, driver):
        question_six = MainPageScooter(driver)
        question_six.navigate()
        question_six.main_questions_text_rotation()
        question_six.click_question_six()
        question_six_text = question_six.text_question_answer_six()
        assert question_six_text == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже ' \
                                    'если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.description(
        'Проверяем, что при нажатии на седьмой вопрос появляется нужный ответ')
    def test_seventh_question(self, driver):
        question_seven = MainPageScooter(driver)
        question_seven.navigate()
        question_seven.main_questions_text_rotation()
        question_seven.click_question_seven()
        question_seven_text = question_seven.text_question_answer_seven()
        assert question_seven_text == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не " \
                                      "попросим. Все же свои."

    @allure.description(
        'Проверяем, что при нажатии на восьмой вопрос появляется нужный ответ')
    def test_eight_question(self, driver):
        question_eight = MainPageScooter(driver)
        question_eight.navigate()
        question_eight.main_questions_text_rotation()
        question_eight.click_question_eight()
        question_eight_text = question_eight.text_question_answer_eight()
        assert question_eight_text == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
