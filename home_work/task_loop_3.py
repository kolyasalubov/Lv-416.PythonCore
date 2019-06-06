# Роздрукувати всі парні числа менші 100 (написати два варіанти коду: один використовуючи цикл while, а інший з використанням циклу for).

#  with  While

i = 1
while i < 100:
    if i % 2 == 0:
        print(i)
    i += 1


# with for

#
# for i in range(100):
#     if i % 2 == 0:
#         print(i)

# with for
#
# for i in range(0, 100, 2):
#     print(i)