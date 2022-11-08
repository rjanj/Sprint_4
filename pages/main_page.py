import allure
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.main_page_locators import MainPageLocators


class MainPageScooter:
    question_one_text = MainPageLocators.question_one_text
    question_one_answer = MainPageLocators.question_one_answer
    question_two_text = MainPageLocators.question_two_text
    question_two_answer = MainPageLocators.question_two_answer
    question_three_text = MainPageLocators.question_three_text
    question_three_answer = MainPageLocators.question_three_answer
    question_four_text = MainPageLocators.question_four_text
    question_four_answer = MainPageLocators.question_four_answer
    question_five_text = MainPageLocators.question_five_text
    question_five_answer = MainPageLocators.question_five_answer
    question_six_text = MainPageLocators.question_six_text
    question_six_answer = MainPageLocators.question_six_answer
    question_seven_text = MainPageLocators.question_seven_text
    question_seven_answer = MainPageLocators.question_seven_answer
    question_eight_text = MainPageLocators.question_eight_text
    question_eight_answer = MainPageLocators.question_eight_answer
    cookies_accept = MainPageLocators.cookies_accept
    scroll_in_to_questions = MainPageLocators.scroll_to_questions

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем главную страницу Scooter')
    def navigate(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru')

    def scroll_into_questions(self):
        main_questions = self.driver.find_element(*self.scroll_in_to_questions)
        self.driver.execute_script("arguments[0].scrollIntoView();", main_questions)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "Home_FAQ__3uVm4")))

    @allure.step('Открываем первый вопрос')
    def click_question_one(self):
        self.driver.find_element(*self.question_one_text).click()

    @allure.step('Получаем ответ на первый вопрос')
    def text_question_answer_one(self):
        question_one_answer = self.driver.find_element(*self.question_one_answer).text
        return question_one_answer

    @allure.step('Открываем второй вопрос')
    def click_question_two(self):
        self.driver.find_element(*self.question_two_text).click()

    @allure.step('Получаем ответ на второй вопрос')
    def text_question_answer_two(self):
        question_two_answer = self.driver.find_element(*self.question_two_answer).text
        return question_two_answer

    @allure.step('Открываем третий вопрос')
    def click_question_three(self):
        self.driver.find_element(*self.question_three_text).click()

    @allure.step('Получаем ответ на третий вопрос')
    def text_question_answer_three(self):
        question_three_answer = self.driver.find_element(*self.question_three_answer).text
        return question_three_answer

    @allure.step('Открываем четвертый вопрос')
    def click_question_four(self):
        self.driver.find_element(*self.question_four_text).click()

    @allure.step('Получаем ответ на четвертый вопрос')
    def text_question_answer_four(self):
        question_four_answer = self.driver.find_element(*self.question_four_answer).text
        return question_four_answer

    @allure.step('Открываем пятый вопрос')
    def click_question_five(self):
        self.driver.find_element(*self.question_five_text).click()

    @allure.step('Получаем ответ на пятый вопрос')
    def text_question_answer_five(self):
        question_five_answer = self.driver.find_element(*self.question_five_answer).text
        return question_five_answer

    @allure.step('Открываем шестой вопрос')
    def click_question_six(self):
        self.driver.find_element(*self.question_six_text).click()

    @allure.step('Получаем ответ на шестой вопрос')
    def text_question_answer_six(self):
        question_six_answer = self.driver.find_element(*self.question_six_answer).text
        return question_six_answer

    @allure.step('Открываем седьмой вопрос')
    def click_question_seven(self):
        self.driver.find_element(*self.question_seven_text).click()

    @allure.step('Получаем ответ на седьмой вопрос')
    def text_question_answer_seven(self):
        question_seven_answer = self.driver.find_element(*self.question_seven_answer).text
        return question_seven_answer

    @allure.step('Открываем восьмой вопрос')
    def click_question_eight(self):
        self.driver.find_element(*self.question_eight_text).click()

    @allure.step('Получаем ответ на восьмой вопрос')
    def text_question_answer_eight(self):
        question_eight_answer = self.driver.find_element(*self.question_eight_answer).text
        return question_eight_answer

    def main_cookies_accept(self):
        self.driver.find_element(*self.cookies_accept).click()

    def navigate_cookie_scroll(self):
        self.navigate()
        self.main_cookies_accept()
        self.scroll_into_questions()