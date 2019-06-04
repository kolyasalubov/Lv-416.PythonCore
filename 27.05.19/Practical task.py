#Змінній   value_int надайте значення 10,
#                value_float - значення 8.4, 
#                 value_str - "No".
#1.	Змініть значення, збережене у змінній value_int, збільшивши його в 3.5 рази, результат зв'яжіть зі змінною big_int.
#2.	Змініть значення, збережене у змінній value_float, зменшивши його на одиницю, результат зв'яжіть з тією ж змінною.
#3.	Розділіть value_int на value_float, а потім big_int на value_float. Результат даних виразів не прив'язуйте до жодних змінних.
#4.	Змініть значення змінної value_str на "NoNoYesYesYes". При формуванні нового значення використовуйте операції конкатенації (+) і повторення рядка (*).


value_int = int(10)
value_float = float(8.4)
value_str = str("No")
big_int = (value_int*3.5)
print ("big_int ", big_int)
value_float = (value_float - 1)
print ("value_float ", value_float)
print (value_int/value_float)
print (big_int/value_float)
value_str = ((value_str*2)+(3*"Yes"))
print (value_str)
