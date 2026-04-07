import pytest
from src.widget import mask_account_card, get_date

pytest.mark.parametrize("mask_account_card expected", [ # фикстура модуля widget, функции mask_account_card
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"), #Error
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
])

