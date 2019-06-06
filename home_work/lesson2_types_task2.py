"""
Задано чотирицифрове натуральне число.
Знайти добуток цифр цього числа.
Записати число в реверсному порядку.
Посортувати цифри, що входять в дане число
"""

num = int(input("Input number from 0001 to 9999: "))
if len(str(num)) < 4 or len(str(num)) > 4:
    print("Number is too short or too long")

res1 = num % 10
rez1 = num // 10

res2 = rez1 % 10
rez2 = rez1 // 10

res3 = rez2 % 10
rez3 = rez2 // 10

res4 = rez3 % 10
rez4 = rez3 // 10

dobutok = res4 * res3 * res2 * res1
number = str(res4) + str(res3) + str(res2) + str(res1)
revers = number[::-1]

print("dobutok of number {} is {}".format(num,dobutok))
print("reverse of number {} is {}".format(num, revers))
print(sorted(str(number)))



#print(res4,res3,res2,res1, end="")