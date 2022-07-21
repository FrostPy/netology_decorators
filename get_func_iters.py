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

class FlatIterator:

    def __init__(self, lists):
        self.lists = lists

    def __iter__(self):
        self.list_iter = iter(self.lists)  # то чем мы ходим по списку
        self.nested_list = []  # список для добавления элементов
        self.cursor = -1  # вынесение курсора за границу списка
        return self

    def __next__(self):
        self.cursor += 1
        if len(self.nested_list) == self.cursor:  # если длина вложенного равна курсору то обнуляем значение курсора
            self.nested_list = None
            self.cursor = 0
            while not self.nested_list:  # если вложенные списки закончились, то получаем stop iteration
                self.nested_list = next(self.list_iter)  
        return self.nested_list[self.cursor]

@get_log_decorator
def list_generator(my_list):
    for list in my_list:
        for item in list:
            yield item


if __name__ == '__main__':

    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    for item in FlatIterator(nested_list):
        print(item)

    print('Списковое включение')
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    
    print('Вызов генератора')
    for item in list_generator(nested_list):
        print(item)


