import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage


class TestOrderPage:
    @allure.title("Тест оформления заказа по клику на кнопку 'Заказать' вверху страницы (набор данных[ #1])")
    @allure.description('''1) Вверху главной странице кликаем на кнопку "Заказать";
                            2) Заполняем данные на странице "Для кого самокат";
                            3) Кликаем на кнопку "Далее";
                            4) Заполняем данные "Про аренду";
                            5) Кликаем на кнопку "Заказать";
                            6) В сплывающем окне подтаерждаем заказ по кнопке "Да";
                            4) Проверяем открытие окна с текстом оформления заказа.''')

    def test_place_an_order_one(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        main_page.click_header_order_button()
        order_page.filling_order_form()
        order_page.filling_order_form_next()
        assert 'Заказ оформлен' in order_page.page_set_order()

    @allure.title("Тест оформления заказа по клику на кнопку 'Заказать' вверху страницы (набор данных[ #2])")
    @allure.description('''1) Вверху главной странице кликаем на кнопку "Заказать";
                            2) Заполняем данные на странице "Для кого самокат";
                            3) Кликаем на кнопку "Далее";
                            4) Заполняем данные "Про аренду";
                            5) Кликаем на кнопку "Заказать";
                            6) В сплывающем окне подтаерждаем заказ по кнопке "Да";
                            4) Проверяем открытие окна с текстом оформления заказа.''')

    def test_place_an_order_two(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        main_page.click_header_order_button()
        order_page.filling_order_form()
        order_page.filling_order_form_next()
        assert 'Заказ оформлен' in order_page.page_set_order()

    @allure.title("Тест оформления заказа по клику на кнопку 'Заказать' внизу страницы (набор данных[ #1])")
    @allure.description('''1) Внизу главной странице кликаем на кнопку "Заказать";
                                2) Заполняем данные на странице "Для кого самокат";
                                3) Кликаем на кнопку "Далее";
                                4) Заполняем данные "Про аренду";
                                5) Кликаем на кнопку "Заказать";
                                6) В сплывающем окне подтаерждаем заказ по кнопке "Да";
                                4) Проверяем открытие окна с текстом оформления заказа.''')

    def test_down_an_order_one(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        main_page.click_order_down_button()
        order_page.filling_order_form()
        order_page.filling_order_form_next()
        assert 'Заказ оформлен' in order_page.page_set_order()

    @allure.title("Тест оформления заказа по клику на кнопку 'Заказать' внизу страницы (набор данных[ #2])")
    @allure.description('''1) Внизу главной странице кликаем на кнопку "Заказать";
                                    2) Заполняем данные на странице "Для кого самокат";
                                    3) Кликаем на кнопку "Далее";
                                    4) Заполняем данные "Про аренду";
                                    5) Кликаем на кнопку "Заказать";
                                    6) В сплывающем окне подтаерждаем заказ по кнопке "Да";
                                    4) Проверяем открытие окна с текстом оформления заказа.''')

    def test_down_an_order_two(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        main_page.click_order_down_button()
        order_page.filling_order_form()
        order_page.filling_order_form_next()
        assert 'Заказ оформлен' in order_page.page_set_order()
