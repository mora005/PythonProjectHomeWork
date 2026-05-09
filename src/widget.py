from .masks import get_mask_account, get_mask_card_number


def mask_account_card(some_info: str) -> str:
    """Принимает на вход номер счёта или карты, маскирует в зависимости от входных данных"""
    part_name = some_info.split()
    number = part_name[-1]
    together = " ".join(part_name[:-1])
    if together == "Счет":
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)
    return f"{together} {masked_number}"


def get_date(date_not_revite: str) -> str:
    """Принимает на вход дату формата "2024-03-11Т02:26:18.671407" и возвращает в формате
    "ДД.ММ.ГГГГ" ("11.03.2024")."""
    day = date_not_revite[8:10]
    month = date_not_revite[5:7]
    year = date_not_revite[:4]
    if day.isdigit() and month.isdigit() and year.isdigit():
        return f"{day}.{month}.{year}"
    else:
        raise ValueError("Ошибка, проверьте формат вводимой даты")
