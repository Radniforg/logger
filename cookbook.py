from Cook.logger_script import logger

keyholder = ['Ingredient_name', 'quantity', 'measure']

@logger('Log/')
def shop_list(dishes_list, person_amount, recipe_book):
    to_buy_list = {}
    for dish in dishes_list:
        dish = dish.capitalize()
        list_to_decompose = recipe_book.get(dish, f'Ошибка: такого блюда нет.\n')
        if 'Ошибка' in list_to_decompose:
            user_answer = input(' Продолжить y/n?\n')
            if user_answer.lower() == 'y':
                continue
            elif user_answer.lower() == 'n':
                print('Ошибка: некорректно введенное название блюда')
                return None
            else:
                print('Неопознанная команда')
                return None
        else:
            for ingredient in list_to_decompose:
                if to_buy_list.get(ingredient['Ingredient_name'], 'Error') == 'Error':
                    temporary_dictionary = {'measure': ingredient['measure'],
                                            'quantity': int(ingredient['quantity']) * person_amount}
                    to_buy_list[ingredient['Ingredient_name']] = temporary_dictionary
                else:
                    to_buy_list[ingredient['Ingredient_name']]['quantity'] = to_buy_list[ingredient['Ingredient_name']]['quantity'] + int(ingredient['quantity']) * person_amount
    for key, value in to_buy_list.items():
        print(f'{key}: {value}')
    return to_buy_list


def cook_book_writing(recipe_file):
    cook_book = {}
    with open(recipe_file, encoding='utf-8') as recipe_book:
        for line in recipe_book:
            line = line.lstrip('\ufeff')
            temporary_list = []
            for _ in range(int(recipe_book.readline())):
                temporary_dict = {}
                current_ingredient = recipe_book.readline()
                recipe_decompose = current_ingredient.split(' | ')
                recipe_decompose[2] = recipe_decompose[2].rstrip()
                for cycle in range(3):
                    temporary_dict[keyholder[cycle]] = recipe_decompose[cycle]
                temporary_list.append(temporary_dict)
            cook_book[line.strip()] = temporary_list
            recipe_book.readline()
    return cook_book

#ниже вывод печати для задачи №1
print(cook_book_writing('recipes.txt'))

#Ниже реализована функция с пользовательским вводом.
user_input = input('Пожалуйста, введите названия блюд через запятую и пробел\n')
buy_list = user_input.split(', ')
try:
    user_amount = int(input('Пожалуйста, введите количество персон:\n'))
    shop_list(buy_list, user_amount, cook_book_writing('recipes.txt'))
except ValueError:
    print('Введено не число')

#Ниже убрана в комментарии реализация функции с вводом списка блюд и количества персон внутри кода:
# user_list = []
# user_amount = 1
# shop_list(buy_list, user_amount)