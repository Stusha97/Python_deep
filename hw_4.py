# 1. Напишите функцию для транспонирования матрицы

# def matrix_change(my_list): 
#     for i in range(len (my_list)):
#         for j in range(len(my_list[i])):
#             print (my_list[j][i], end = ' ')
#         print()

# matrix_1 = [
#     [1,2,3],
#     [10,20,30],
#     [100,200,300]
# ]

# matrix_change (matrix_1)

# 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, 
# а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.

# def func_fruits (**fruits) :
#     fruit ={}
#     for key, value in fruits.items():
#         if value.__hash__ is not None:
#             fruit[value] = key
#         else:
#             fruit[str(value)] = key
#     return fruit

# def func_fruits (**fruits) :
#     return {value if value.__hash__ is not None else str(value):key for key,value in fruits.items()}

# print(func_fruits(bananas = 1,apples = (3,5), oranges = [5,8,9]))


