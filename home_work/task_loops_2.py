# Написати скрипт, який обчислить факторіал введеного числа.


num = int(input("Input natural number: "))

i = 1
fact = 1
while i <= num:
    fact *= i
    i += 1
print ("Factorial of number {} is {}".format(num, fact))