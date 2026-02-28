from masks import get_mask_card_number, get_mask_account


def mask_account_card(some_info: str) -> str:
    '''  Принимает на вход номер счёта или карты, маскирует в зависимости от входных данных '''
    part_name = some_info.split()
    number = part_name[-1]
    together = ' '.join(part_name[:-1])
    if together.upper() == 'Счет':
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)



