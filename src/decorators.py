from binascii import Error
from functools import wraps
from time import time

from typing import Callable, Any


def filename_exist(message: str, filename: str | None = None) -> None:
    if filename:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message)
    else:
        print(message)


def log(filename: str | None = None) -> Callable:
    def log_inside(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:

            try:
                time_before = time()
                result = func(*args, **kwargs)
                time_after = time()
                message = f"time working {time_after - time_before}\n {func.__name__} ok\n"
                filename_exist(message, filename)
                return result
            except Exception as e:
                message = f"{func.__name__} error: {type(e)} Inputs: {args}, {kwargs}\n"
                filename_exist(message, filename)
                raise

        return wrapper

    return log_inside


@log(filename="mylog.txt")
def my_function(x: float, y: float) -> float:
    """Функция, складывающая 2 числа"""
    return x / y


# a = my_function(1, 0)
