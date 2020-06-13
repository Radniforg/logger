import datetime
import inspect
import os


def logger(path_to_file):
    try:
        os.makedirs(path_to_file)
    except FileExistsError:
        pass
    def decorator(some_function):
        function_initiation = str(datetime.datetime.now())
        function_initiation = function_initiation.split('.')[0]
        def new_function(*args, **kwargs):
            logged_function = some_function(*args, **kwargs)
            with open(f'{path_to_file}log_file.txt', 'w') as log:
                log.write(f'Дата и время вызова функции: {function_initiation}\n')
                log.write(f'Имя фунции: {some_function.__name__}\n')
                fullargspec_splitted = str(inspect.getfullargspec(some_function)).split('=')
                for fullargpart in fullargspec_splitted:
                    if 'varargs' in fullargpart:
                        arg_names = fullargpart.split(', v')

                    if 'kwonlyargs' in fullargpart:
                        default = fullargpart.split(', k')
                log.write(f'Аргументы функции: {arg_names[0]}\n')
                log.write(f'Значения по умолчанию: {default[0]}\n')
                frame = inspect.currentframe()
                arg_kwarg = locals()
                log.write(f'Args values: {arg_kwarg["args"]}\n')
                log.write(f'Kwargs values: {arg_kwarg["kwargs"]}\n')
                log.write(f'Вывод функции: {logged_function}')
            return logged_function
        return new_function
    return decorator



# @logger('log/')
# def test_function(с = 3, b = 4):
#     return с+b
#
# z = test_function()
# print(z)
