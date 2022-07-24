from datetime import datetime
import requests


PATH = 'logs.txt'


def get_log_decorator(path):
    def decorator(old_func):
        def new_func(*args, **kwargs):
            date_time = datetime.now()
            func_name = old_func.__name__
            result = old_func(*args, **kwargs)
            with open(path, 'w', encoding='utf-8') as file:
                file.write(f'Дата/время: {date_time}\n'
                           f'Имя функции: {func_name}\n'
                           f'Аргументы: {args, kwargs}\n'
                           f'Результат: {result}\n')
            return result
        return new_func
    return decorator


@get_log_decorator(PATH)
def get_status(*args, **kwargs):
    url = ','.join(args)
    response = requests.get(url=url)
    return response.status_code


if __name__ == '__main__':
    get_status('https://github.com/FrostPy/netology_module_packages')