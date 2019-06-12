"""
Задано чотирицифрове натуральне число.
Знайти добуток цифр цього числа.
Записати число в реверсному порядку.
Посортувати цифри, що входять в дане число
"""

num = int(input("Input number from 1000 to 9999: "))
if len(str(num)) < 4 or len(str(num)) > 4:
    print("Number is too short or too long")

num4 = num % 10
rez1 = num // 10

num3 = rez1 % 10
rez2 = rez1 // 10

num2 = rez2 % 10
rez3 = rez2 // 10

num1 = rez3 % 10
rez4 = rez3 // 10

product = num1 * num2 * num3 * num4
revers_num = str(num)[::-1]

print("Product of number {} is {}".format(num,product))
print("reverse of number {} is {}".format(num, revers_num))
print(sorted(str(num)))