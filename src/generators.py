





def card_number_generator (start: int = 1, stop: int = 9) -> None :
    ''' генератор который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX
Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.'''
    for number in range(start, stop + 1):
        yield (f"{str(number).zfill(16)[:4]} "
               f"{str(number).zfill(16)[4:8]} "
               f"{str(number).zfill(16)[8:12]} "
               f"{str(number).zfill(16)[12:]}")
if __name__ == "__main__":
    for card_number in card_number_generator(1, 99999):
        print(card_number)