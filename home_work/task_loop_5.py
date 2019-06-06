# Перевірити чи список містить непарні числа.
#           (Підказка: використати оператор break)


lis = [2,4,6,8,10,12,14]

for i in lis:
    if i % 2 != 0:
        print(True)
        break
else:
    print (False)