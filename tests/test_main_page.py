import allure
import pytest
import data
from pages.main_page import MainPage


class TestMainPage:
    @allure.title('Тест проверки выподающих ответов в разделе «Вопросы о важном»')
    @allure.description('''1)Скроллим до блока с вопросами;
                            2)Кликаем на вопрос;
                            3)Получаем выподающий ответ на вопрос;
                            4)Сравниваем полученный текст ответа с ожидаемым''')
    @pytest.mark.parametrize(
        'num, result',
        [
        (0, data.answer_question_1),
        (1, data.answer_question_2),
        (2, data.answer_question_3),
        (3, data.answer_question_4),
        (4, data.answer_question_5),
        (5, data.answer_question_6),
        (6, data.answer_question_7),
        (7, data.answer_question_8)
        ]
    )
    def test_questions_and_answer(self, driver, num, result):
        main_page = MainPage(driver)
        assert result == main_page.get_answer_text(num)

