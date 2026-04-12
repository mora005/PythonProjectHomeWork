from src.masks import get_mask_card_number, get_mask_account
import pytest


def test_get_mask_card_number():
    """Функция тестирующая различные сценарии ввода у функции
    get_mask_card_number из модуля masks.py"""
    assert get_mask_card_number(1234567891234567) == "1234 56** **** 4567"

    assert get_mask_card_number("1234567812345678") == "1234 56** **** 5678"
    with pytest.raises(ValueError):
        get_mask_card_number("1qas4rfgt6")
    with pytest.raises(ValueError):
        get_mask_card_number("")


def test_get_mask_account():
    """Функция тестирующая различные сценарии ввода у функции
    get_mask_account из модуля masks.py"""
    assert get_mask_account(12345678112345678123) == "**8123"
    with pytest.raises(ValueError):
        get_mask_account(123456)
    with pytest.raises(ValueError):
            get_mask_account("1a11d323d")

