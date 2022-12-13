# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# |||||||||||||||||||||||||||||||||
# my_list = [2, 3, 5, 9, 3,1,1,0,3]
# res = 0
# for item in range(1, len(my_list), 2):
#     res += my_list[item]
# print(f'Список чисел {my_list}')
# print(f'Сумма элементов списка, стоящих на нечетной позиции = {res}')
# Улучшенный способ
# def result(lst):
#     res = []
#     lst =  [i for i in range(1,len(lst), 2) if res.append(lst[i])]
#     return res
# odd_list = result([2, 3, 5, 9, 3])
# print(sum(odd_list))

# # Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# text = 'фывфывабв зыдвыфв абвфывф абв фывфыв фывфабфыф'
# search_str = "абв"
# list = text.split()
# my_list = []
# print(list)
# for i in range(len(list)):
#     if search_str not in list[i]:
#         my_list.append(list[i])
# print(my_list)
#  Улучшенный способ
# text = 'фывфывабв зыдвыфв абвфывф абв фывфыв фывфабфыф'
# search_str = "абв"
# list = text.split()
# my_list = [i for i in text.split() if search_str not in i]
# print(f'{" ".join(my_list)}')

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
# if a**2 == b:
#     print('Второе число является квадратом первого5')
# elif b**2 == a:
#     print('Первое число является квадратом второго')
# else:
#     print('Квадратов нет')
# Решение с lambda
def square(op,x,y):
        print(f'{y} в степени 2 = {op(x,y)} . Значит второе число квадрат первого')
def square1(op,x,y):
        print(f'{x} в степени 2 = {op(x,y)} . Значит первое число квадрат второго')
if a**2 == b:
        print(square1(lambda s,d: s**2, a,b ))
elif b**2 == a:
        print(square(lambda s,d: d**2, a,b ))
else:
     print('Квадратов нет')
