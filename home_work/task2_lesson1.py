"""Please create a console script in Python:
write code for solving next tasks:
Define integer variables a and b. Read values a and b from console and calculate:
a + b
a - b
a * b
a / b.
Output obtained results.
Output question “What is your name?“, “How old are you?“, Where do you live?“.
Read the answer of user and output next information: “Hello, (answer)“, “Your age is  (answer)“, “You live in  (answer)“"""



a = int(input("input first number: "))
b = int(input("input second number:"))
znak = input("Chouse your operation\" + - * / \"  ")


if znak == "+":
    res = a+b
elif znak == "-":
    res = a-b
elif znak == "*":
    res = a*b
elif znak == "/":
    res = a/b
else:
    print("Your caracter is wrong")
print("{}{}{} = ".format(a,znak,b), res)