#Змінній   value_int надайте значення 10,
#                value_float - значення 8.4, 
#                 value_str - "No".
#1.	Змініть значення, збережене у змінній value_int, збільшивши його в 3.5 рази, 
# результат зв'яжіть зі змінною big_int.
#2.	Змініть значення, збережене у змінній value_float, зменшивши його на одиницю, 
# результат зв'яжіть з тією ж змінною.
#3.	Розділіть value_int на value_float, а потім big_int на value_float. Результат 
# даних виразів не прив'язуйте до жодних змінних.
#4.	Змініть значення змінної value_str на "NoNoYesYesYes". При формуванні нового 
# значення використовуйте операції конкатенації (+) і повторення рядка (*).


# value_int = int(10)
# value_float = float(8.4)
# value_str = str("No")
# big_int = (value_int*3.5)
# print ("big_int ", big_int)
# value_float = (value_float - 1)
# print ("value_float ", value_float)
# print (value_int/value_float)
# print (big_int/value_float)
# value_str = ((value_str*2)+(3*"Yes"))
# print (value_str)

# # перевірити яке з двох чисел більше

# a = float(input("Input first number: "))
# b = float(input("Input second number: "))
# if a==b:
#     print ("First number: ",a,"Second number: ",b," Both numbers are equal!")
# elif a<b:
#     print ("First number: ",a,"Second number: ",b," The second number is more!")
# else:
#     print ("First number: ",a,"Second number: ",b," First number more!")


# # 2.	Написати скрипт, який перевірить чи введене число парне чи непарне і вивести відповідне 
# # повідомлення.

# input_number = int(input("Input number: "))
# if input_number%2==0:
#     print ("The number: {} is paired!".format(input_number))
# else:
#     print ("The number: {} no paired!".format(input_number))


# # 3.	Написати скрипт, який обчислить факторіал введеного числа.

# input_number = int(input("Input natural number: "))
# i = 1
# fact = 1
# while i <= input_number: 
#     fact *= i
#     i += 1
# print("Factorial {}! ={}".format(input_number,fact))


# # 1.	Роздрукувати всі парні числа менші 100 
# # (написати два варіанти коду: один використовуючи цикл while, а інший з використанням циклу for).

# i = 0
# while i<100:
#     if i % 2 == 0:
#         print(i)
# #     i = i + 1
# #####################################
# # for i in range(100):
# #     if i % 2 == 0:
# #         print(i)
# ###################################
# for i in range(0,100,2):
#     print(i)

# Роздрукувати всі непарні числа менші 100. (написати два варіанти коду: 
# # один використовуючи оператор continue, а інший без цього оператора).

# for item in range(100):
#     if item % 2 == 0:
#         continue
#     print(item)
# ################################
# for item in range(1,100,2):
#     print(item)


# # 3.	Перевірити чи список містить непарні числа.
# #           (Підказка: використати оператор break)

# list_number=[2,4,6,8,9,10]
# contain_odd=False
# for i in list_number:
#     if not i % 2 == 0: 
#         contain_odd=True
#         break
# if contain_odd:
#     print("There is odd number in the list")
# else: 
#     print("There is only even number in the list")


# 4.	Створити список, який містить елементи цілочисельного типу, потім 
# за допомогою циклу перебору змінити тип даних елементів на числа з плаваючою крапкою. 
# # (Підказка: використати вбудовану функцію float ()).

# list_number = [2,3,4,5,6,7,8,8,9,12]
# element = []
# for i in list_number:
#     element.append(float(i))
# list_number = element
# print(list_number)
# # # 5.	Вивести числа Фібоначі включно до введеного числа n, використовуючи цикли. 
# # # (Послідовність чисел Фібоначі 0, 1, 1, 2, 3, 5, 8, 13 і т.д.)

# n=int(input('enter some number from fibonacci list='))
# fibonacci_numbers = [0, 1]
# for i in range(2,n):
#     fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
#     if fibonacci_numbers[i]==n:
#         break
# print('there are some numbers from fibanacci till that you entered',n,'\n',fibonacci_numbers)

# # 6.	Створити список, що складається з чотирьох елементів типу string. Потім, 
# # за допомогою циклу for, вивести елементи по черзі на екран.

# List_elements = ['ta','po','ha','be']
# for i in List_elements:
#     print(i)

# 7.	Змінити попередню програму так, щоб в кінці кожної букви елементів при виводі додавався певний символ, наприклад “#”. 
#           (Підказка: цикл for може бути вкладений в інший цикл, а також  треба використати функцію print(“ ”, end=”%”)).

# List_elements = ['ta','po','ha','be']
# for i in List_elements:
#     for j in i:
#         print(j,end='#')
# # print(i)

# 8.	Юзер вводить число з клавіатури, написати скріпт, який визначає чи це число просте чи складне.

# input_namber = int(input("Your number: "))
# if 

# 9.	Знайти максимальну цифру дійсного числа. Дійсне число генеруємо випадковим чином за допомогою методу random() з модуля random
# (для цього підключаємо модуль random наступним чином 
# from random import random)
# from random import random


# 10.	Визначити чи введене слово паліндром, тобто чи воно читається однаково зліва направо і навпаки.


# 1.	Створити список цілих чисел, які вводяться з терміналу та визначити серед них 
# максимальне та мінімальне число.

# number_user = int(input("input your number: "))
# list = []
# i = 1
# while i <= number_user:
#     item = input("Input your tekst: ")
#     i += 1
#     list.append(item)
# # print(list)

# number_user = int(input("input your number: "))
# list = []
# for i in range(number_user):
#     item = input("Input your text: ")
# #     list.append(item)
# # print(list)

# value = [ for value in range(int(input("input your number: "))) item = input("Input your text: ") list.append(item)]

