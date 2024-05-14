import allure
from locators.the_main_page_locators import MainPageLocators
from pages.base_page import BasePage


class RedirectPage(BasePage):

    @allure.step('нажимаем на кнопку "Заказать" на главной странице, потом на логотип "Самокат" на странице заказа')
    def scooter_logo_redirect(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_HEADER)
        self.click_on_element(MainPageLocators.SCOOTER_LOGO)
        return self.get_text_from_element(MainPageLocators.HOME_HEADER)

    @allure.step('нажимаем на логотип "Яндекс" на главной странице, перходи на нову вкладку браузера')
    def yandex_logo_redirect(self):
        self.click_on_element(MainPageLocators.YANDEX_LOGO)
        self.switch_to_window()
        dzen_logo = self.find_element_with_wait(MainPageLocators.DZEN_LOGO)
        return dzen_logo
