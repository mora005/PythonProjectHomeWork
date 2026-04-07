from src.widget import mask_account_card, get_date
import pytest

def test_mask_account_card():
    ''' Функция тестирующая различные сценарии ввода у функции
    mask_account_card из модуля widget.py'''
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"

    assert mask_account_card("Счет 64686473678894779589") == "Счет **9589" #error

    assert mask_account_card("1лвц8947ук7щв9") == "Ошибка, проверьте правильность ввода номера карты"


def test_get_date():
    ''' Функция тестирующая различные сценарии ввода у функции
    get_date из модуля widget.py '''
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"

    #assert get_date("204-5-12:26:18.6") == "Ошибка, проверьте формат вводимой даты"

    assert get_date("2н024-ар03-1о1T02ва407") == "Ошибка, проверьте формат вводимой даты"
