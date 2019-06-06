# Написати скрипт, який перевірить чи введене число парне чи непарне і вивести відповідне повідомлення.


num = int(input("input your namber: "))
if num % 2 == 0:
     print ("number {} is eval.".format(num))

else: print ("number {} is odd".format(num))
