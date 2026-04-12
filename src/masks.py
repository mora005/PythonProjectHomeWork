from typing import Union


def get_mask_card_number(card_num: Union[str, int]) -> Union[str]:
    """Функция принимающая на вход номер карты"""
    card_str = str(card_num)
    if len(card_str) == 16:
        mask = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
        return mask
    else:
        raise ValueError("Ошибка, проверьте правильность ввода номера карты")


# возвращает замаскированый номер карты


def get_mask_account(bank_num: int | str) -> str:
    """Функция принимающая на вход номер счёта"""
    bank_str = str(bank_num)
    if len(bank_str) == 20:
        masked = f"**{bank_str[-4:]}"  # 73654108430135874305
        return masked
    raise ValueError("Oшибка, проверьте правильность ввода номера счёта")


# возвращает замаскированный банковский счёт
