from typing import Dict, List


def filter_by_state(user_information: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Функция принимает список словарей и значение для ключа
    state(по умолчанию 'EXECUTED') возвращая новый список словарей,
    содержащий только те словари, у которых ключ state соответствует указанному значению."""
    filter_dicts = []
    for filter_dict in list_dicts:
        if filter_dict.get("state") == state:
            filter_dicts.append(filter_dict)

    return filter_dicts


# list_dicts = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
# {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
# {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
# {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def sort_by_date(user_dict: List[Dict[str, Any]], date: bool = True) -> List[Dict[str, Any]]:
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание) возвращает новый список, отсортированный по дате."""
    sorted_dates = sorted(user_dict, key=lambda x: x["date"], reverse=date)
    return sorted_dates
