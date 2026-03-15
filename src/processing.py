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
    возвращает новый список словарей, отсортированный по дате возрастания."""
    sorted_dates = sorted(user_dict, key=lambda x: x["date"], reverse=not date)
    return sorted_dates
