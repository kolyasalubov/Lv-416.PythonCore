
wordList=["Maria","Roman","Oleg","Ostap"]
for i in wordList:
    newList=[j+"#" for j in i]
    i ="".join(newList)
    print(i)
############################################################################################################
import random # max element from a list

newList=[random.randrange(1,100) for i in range(int(input("Input number of elements in list: ")))]
print(newList)
print("Max number in a list is: ",max(newList))
############################################################################################################
number = int(input("input some number: "))     # Task: recognize folded or simple number from input!

if number>1 and  number%2==1 or number==2:
    print("number is simple") 
elif number<=1 :
    print("Number is not folded and not simple")
elif number>2 and number%2==0:
    print("number is folded")
############################################################################################################
numberList=[int(input("Input number into a list: ")) for i in range(3)] # Output biggest and smallest number from input
print("The biggest number in a list is: {}\nThe smallest number in a list is: {}".format(max(numberList),min(numberList)))
############################################################################################################
word=input("Input some word:") #Checkout if the word is palindrom!

if word.lower()==word[::-1].lower():
    print("Inputed word is palindrom!")
else:
    print("Inputed word isnt palindrom!")
############################################################################################################
numberList=[i+1 for i in range(10)] # i%2 i%3 i!=%2 and i!=%3
dev2List=[]
dev3List=[]
deferList=[]
for i in numberList:
    if i%2==0:
        dev2List.append(i)
    if i%3==0:
        dev3List.append(i)
    if i%2!=0 and i%3!=0:
        deferList.append(i)
print("Numbers can be deveded by 2 from 1..10 is:",dev2List,"\n")
print("Numbers can be deveded by 3 from 1..10 is:",dev3List,"\n")
print("Numbers cant be devided by 2 an 3 from 1..10 is:",deferList,"\n")