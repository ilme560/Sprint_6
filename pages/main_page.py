import allure
from locators.the_main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step(' Получаем текст ответа ')
    def get_answer_text(self, num):
        self.scroll_to_element(MainPageLocators.BLOCK_OF_QUESTION_LOCATOR)
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER, num)
        self.click_on_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step(' Кликаем на кнопку "Заказать" в вверху страницы и получаем текст в хедере открывшейся страницы ')
    def click_header_order_button(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_HEADER)
        return self.get_text_from_element(OrderPageLocators.ORDER_HEADER)

    @allure.step(' Кликаем на кнопку "Заказать" внизу страницы и получаем текст в хедере открывшейся страницы ')
    def click_order_down_button(self):
        self.scroll_to_element(MainPageLocators.BLOCK_OF_QUESTION_LOCATOR)
        self.click_on_element(MainPageLocators.ORDER_BUTTON_DOWN)
        return self.get_text_from_element(OrderPageLocators.ORDER_HEADER)
