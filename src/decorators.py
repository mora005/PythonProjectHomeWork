from binascii import Error
from functools import wraps
from time import time


def log(filename=None) -> None:
    def log_inside(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time_before = time()
            result = func(*args, **kwargs)
            time_after = time()
            print(f"time working {time_after - time_before}")

            try:
                func(*args, **kwargs)
            except Exception as e:
                print(f"{func.__name__} error: {e} Inputs: {args}, {kwargs}")
            else:
                print(f"{func.__name__} ok")

        return wrapper

    return log_inside


@log(filename="mylog.txt")
def my_function(x, y):
    '''Функция, складывающая 2 числа'''
    return x + y


my_function(1, 2)
