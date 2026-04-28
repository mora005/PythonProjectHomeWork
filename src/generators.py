def filter_by_currency(transactions, currency_code) -> None:
    """функция которая принимает на вход список словарей, представляющих транзакции.
    возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    return (
        transaction
        for transaction in transactions
        if transaction["operationAmount"]["currency"]["code"] == currency_code
    )


for transaction in transactions:
    usd_transactions = filter_by_currency(transactions, "USD")
if __name__ == "__main__":
    for parts in range(2):
        print(next(usd_transactions))
else:
    raise ValueError


def transaction_descriptions(transactions):
    """генератор который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction["description"]


descriptions = transaction_descriptions(transactions)
if __name__ == "__main__":
    for _ in range(5):
        print(next(descriptions))
else:
    raise ValueError


def card_number_generator(start: int = 1, stop: int = 9) -> None:
    """генератор который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    for number in range(start, stop + 1):
        yield (
            f"{str(number).zfill(16)[:4]} "
            f"{str(number).zfill(16)[4:8]} "
            f"{str(number).zfill(16)[8:12]} "
            f"{str(number).zfill(16)[12:]}"
        )


if __name__ == "__main__":
    for card_number in card_number_generator(1, 99999):
        print(card_number)
else:
    raise ValueError
