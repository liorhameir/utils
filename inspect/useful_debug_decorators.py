from typing import Callable
from functools import wraps


def custom_profile(func: Callable) -> Callable:
    """
    takes/wraps a Callable and profiles its calls
    :param func: callable
    :return: wrapper
    """
    import cProfile
    @wraps(func)
    def wrapper(*args, **kwargs):
        prof = cProfile.Profile()
        retval = prof.runcall(func, *args, **kwargs)
        prof.print_stats()
        return retval
    return wrapper


def logger(func: Callable) -> Callable:
    """
    takes/wraps a Callable and documents its calls by args and kwargs
    :param func: callable
    :return: wrapper
    """
    import logging
    logging.basicConfig(filename=f'{func.__name__}.log', level=logging.INFO)
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

