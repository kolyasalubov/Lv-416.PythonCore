# Поміняти між собою значення двох змінних,
# не використовуючи третьої змінної

print("foo = 2, bar = 5")

foo, bar = 2, 5
foo, bar = bar, foo

print("after coding: foo = {0}, bar = {1}".format(foo, bar))