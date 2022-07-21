from datetime import datetime
import requests


def get_log_decorator(old_func):
    def new_func(*args, **kwargs):
        date_time = datetime.now()
        func_name = old_func.__name__
        result = old_func(*args, **kwargs)
        with open('logs.txt', 'w', encoding ='utf-8') as f:
            f.write(f'Дата/время:{date_time}\n'
                    f'Название функции: {func_name}\n'
                    f'Аргументы функции: {args, kwargs}\n'
                    f'Результат: {result}\n')
        return result
    return new_func
