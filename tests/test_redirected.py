import allure
from pages.redirected_page import RedirectPage


class TestRedirectPage:
    @allure.title('Тест проверки перехода на главную страницу "Яндекс.Самокат" по клику на логотип "Самокат"')
    @allure.description(''' 1)Кликаем на кнопку "Заказать"
                            2)Кликаем на логотип "Самокат"
                            3)Проверяем наличие текста в описании заголовка''')
    def test_logo_scooter_redirect(self, driver):
        redirect_page = RedirectPage(driver)
        assert 'Привезём его прямо к вашей двери,' in redirect_page.scooter_logo_redirect()

    @allure.title('Тест проверки перехода на "Яндекс.Дзен" по клику на логотип "Яндекса"')
    @allure.description(''' 1)Кликаем на логотип "Яндекс"
                            2)Переходим на новую вкладку браузера
                            3)Проверяем отображение элемента "Главная" для подтверждения перехода ''')
    def test_ya_logo_redirect(self, driver):
        redirect_page = RedirectPage(driver)
        assert redirect_page.yandex_logo_redirect().is_displayed(), "Элемент отображается на странице"
