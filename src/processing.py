from typing import Dict, List
from typing import Any


def filter_by_state(list_dicts: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Функция принимает список словарей и значение для ключа
    state(по умолчанию 'EXECUTED') возвращая новый список словарей,
    содержащий только те словари, у которых ключ state соответствует указанному значению."""
    filter_dicts = []
    for filter_dict in list_dicts:
        if filter_dict.get("state") == state:
            filter_dicts.append(filter_dict)

    return filter_dicts


def sort_by_date(user_dict: List[Dict[str, Any]], date: bool = True) -> List[Dict[str, Any]]:
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки,
    возвращает новый список словарей, отсортированный по дате убывания."""
    sorted_dates = sorted(user_dict, key=lambda x: x["date"], reverse=True)
    return sorted_dates

if __name__ == "__main__":
    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]))
