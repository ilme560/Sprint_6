from selenium.webdriver.common.by import By


class MainPageLocators:
    # кнопка "Яндекс" в хедере сайта
    YANDEX_LOGO = By.CLASS_NAME, 'Header_LogoYandex__3TSOI'
    # кнопка "Самокат" в хедере сайта
    SCOOTER_LOGO = By.CLASS_NAME, 'Header_LogoScooter__3lsAR'
    # надпись "Дзен" на главной странице сайта Дзен
    DZEN_LOGO = By.ID, 'dzen-header'
    # надпись "Самокат на пару дней" на главной странице сайта Яндекс Самокат
    HOME_HEADER = By.CLASS_NAME, 'Home_Header__iJKdX'
    # кнопка "Заказать" вверху сайта Яндекс Самокат
    ORDER_BUTTON_HEADER = By.CLASS_NAME, 'Button_Button__ra12g'
    # кнопка "Заказать" внизу сайта Яндекс Самокат
    ORDER_BUTTON_DOWN = By.XPATH, './/div[5]/button[text() = "Заказать"]'
    # надпись "Вопросы о важном" на главной странице сайта Яндекс Самокат
    QUESTIONS_ABOUT = By.CLASS_NAME, 'Home_SubHeader__zwi_E'
    # кнопки с вопросами в блоке "Вопросы о важном"
    QUESTION = By.XPATH, '//*[@id="accordion__heading-{}"]'
    # строки с ответами "Вопросы о важном"
    ANSWER = By.XPATH, '//*[@id="accordion__panel-{}"]'
    # блок "Вопросы о важном"
    BLOCK_OF_QUESTION_LOCATOR = By.CSS_SELECTOR, '[class *="Home_FourPart"]'
