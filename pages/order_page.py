import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from helpers import get_sign_up_date
from data import UserData


class OrderPage(BasePage):

    @allure.step('Заполняем первую страницу формы заказа и нажимаем на кнопку "Далее"')
    def filling_order_form(self):
        name, last_name, address = get_sign_up_date()
        self.add_text_to_element(OrderPageLocators.NAME_FIELD, name)
        self.add_text_to_element(OrderPageLocators.SURNAME_FIELD, last_name)
        self.add_text_to_element(OrderPageLocators.ADDRESS_FIELD, address)
        self.add_text_to_element(OrderPageLocators.METRO_STATION_FIELD, UserData.METRO_STATION)
        self.click_on_element(OrderPageLocators.ADD_STATION)
        self.add_text_to_element(OrderPageLocators.TELEPHONE_FIELD, UserData.PHONE_NUMBER)
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполняем вторую страницу формы заказа и нажимаем на кнопку "Заказать" и кнопку "Да" в сплывающем окне подтверждения заказа')
    def filling_order_form_next(self):
        self.click_on_element(OrderPageLocators.DATA_FIELD)
        self.add_text_to_element(OrderPageLocators.DATA_FIELD, UserData.DAY_OF_ORDER)
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        self.click_on_element(OrderPageLocators.PERIOD_BUTTON)
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)
        self.click_on_element(OrderPageLocators.YES_BUTTON)

    @allure.step('Проверяем окно оформленного заказа')
    def page_set_order(self):
        return self.get_text_from_element(OrderPageLocators.ORDER_PLACED)
