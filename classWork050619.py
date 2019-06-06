number = int(input("Input some number: "))
if number%2==0 :
    print("Number {} is pair ".format(number))
else:
    print("Number {} isnt pair".format(number))
#############################################################################
num=int(input("Input natural number: "))
i=1
fact=1
while i <= num: 
    fact *= i
    i += 1
    print(fact)
print("Factorial {}! =".format(num), fact)
#############################################################################
numberList=[]
i=1
for i in range(1,101):
    if i%2==0:
        numberList.append(i)
    i+=1
print(numberList)

#############################################################################
numberList=range(1,100)
evenNumberList=[]
for i in numberList:
    if i%2==1:
        evenNumberList.append(i)
        print(i)
print(evenNumberList)
#############################################################################
evenList=[]
for i in range(1,100):
    if i%2==0:         # we can chenge 'if i%2==1:' and we got even numbrs
        continue
    evenList.append(i)
    print(i)
print(evenList)
#############################################################################
listNumber=[1,100]
for i in listNumber:
    if i%2==1:
        break
    print("The list contain odd numbers!!!")
#############################################################################
import random
listNumber=[]
i=1
while i<=10:
    randNumber=random.randrange(1,10)
    listNumber.append(randNumber)
    i+=1
print("Random created list= {}\n ".format(listNumber))
for n,i in enumerate(listNumber):
    if int(i):
        listNumber[n]=float(i)
print("Transformed list= {}".format(listNumber))
#############################################################################
wordList=["Maria","Roman","Oleg","Ostap"]
for i in wordList:
    print(i)
#############################################################################
number=int(input("Input some number: "))
print(0)
print(1)
num1=0
num2=1
i=1
while i<number:
    fibonachi=num1+num2
    num1=num2
    num2=fibonachi
    print(fibonachi)
    i+=1
#############################################################################










