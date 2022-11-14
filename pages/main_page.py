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

    def main_cookies_accept(self):
        self.driver.find_element(*self.cookies_accept).click()

    def navigate_cookie_scroll(self):
        self.navigate()
        self.main_cookies_accept()
        self.scroll_into_questions()

    def click_question_and_take_answer(self, click, question):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "Home_FAQ__3uVm4")))
        self.driver.find_element(*click).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(question))
        question_answer = self.driver.find_element(*question).text
        return question_answer
