# 2. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

# def func_1 (reference:str):
#     file_name_path,file_extension = reference.split('.')
#     last_symb = file_name_path.rfind('/')    #находит индекс последнего вхождения элемента
#     file_path,file_name = file_name_path[:last_symb], file_name_path.split('/')[-1]
#     return file_path,file_name,file_extension

# file = "C:/Users/A/OneDrive/Geekbrains/Python.pdf"
# print(func_1(file))

# 3. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
# имена str, ставка int, премия str с указанием процентов вида “10.25%”. 
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии

# names = ['Bob', 'Max', 'Alex', 'Danny']
# rates = [10000,15000,26000,35000]
# rewards = ['5.5%', '7.5%', '2.3%','4.2%']
# my_dict = {name:rate*(float(reward[:-1])/100) for name,rate,reward in zip(names,rates,rewards)}
# print(my_dict)


# 4. Создайте функцию генератор чисел Фибоначчи

# def fibonachi (n):
#     result,i = 0,1
#     for _ in range (n):
#         yield result
#         result,i = i,result+i
        
# for i in (fibonachi(6)):
#     print (i, end = ' ')