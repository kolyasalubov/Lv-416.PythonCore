number = int(input('Input some number: '))

n1=int(number/1000)                  # found first element in order
n2=int((number-n1*1000)/100)         # found second element in order
n3=int((number-(n1*1000+n2*100))/10) # found third element in order
n4=number%10                         # found fourth element in order
if n1 and n2 and n3 and n4 :         # checking if some of elements isnt 0
    elementsMultiplication=n1*n2*n3*n4
    print("Multiplication of number elevents is: ",elementsMultiplication)
else:
    print("Some elements of number is zero! Result of multiplication will be 0")
reverseNumber = "{}{}{}{}".format(n4,n3,n2,n1)
print("Reverse number is:",reverseNumber)

numberList=[int(number) for number in str(number)]
numberList.sort()
for i in numberList:
    print(i,end='')

