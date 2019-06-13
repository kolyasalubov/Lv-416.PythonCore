def find_avarage(*args):
    """ This fanction counts middle avarage of numbers"""
    sum=0
    count=0
    for i in args :
        sum+=int(i)
        count+=1
    return sum/count    
print("avarage is :",int(find_avarage(11,10,12)))
###########################################################################################################
def absFunc(number):
    """This function returns the absolute value of number"""
    if number>=0:
        return number
    else:
        return -number
print(absFunc(-9))  
############################################################################################################
def maxNumber():
    """That function show the greatest number from the two inputed numbers!"""
    x, y = [int(x) for x in input("Input two numbers: ").split()] 
    if x > y:
        return print("Number {} is greater than {}".format(x,y))
    elif x < y:
        return print("Number {} is greater than {}".format(y,x))
print(maxNumber())
############################################################################################################
import pyowm

city=input("Введіть місто яке вам потрібно: ")
owm = pyowm.OWM('ef2206ff5da67de63306d0b143e20872')  # You MUST provide a valid API key

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Search for current weather in London (Great Britain)
observation = owm.weather_at_place(city)
w = observation.get_weather()                     # <Weather - reference time=2013-12-18 09:20,
#print(w)                              # status=Clouds>

# Weather details
w.get_wind()                  # {'speed': 4.6, 'deg': 330}
w.get_humidity()              # 87
w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
maxTemp=w.get_temperature('celsius')['temp_max']
minTemp=w.get_temperature('celsius')['temp_min']
midTemp=maxTemp/minTemp
#middleTemp=maxTemp/minTemp
print('cool',minTemp)
print("Максимальна температура у {} є {}".format(city,maxTemp))
print("Середня температура у {} є {}".format(city,midTemp))

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
observation_list = owm.weather_around_coords(-22.57, -43.12)
#############################################################################################################
def triangleSquare():
    """Function calculating triangle square"""
    triangleSide=int(input("Input side of triangle: "))
    triangleHeight=int(input("Input height on to side of triangle:"))
    s=0.5*triangleSide*triangleHeight
    print("\nTriangle square is equal to ",s)
def rectangleSquare():
    """Function calculating rectangle square"""
    rectangleSide1,rectangleSide2=[int(i) for i in input("Input sides of rectangle: ").split()]
    # rectangleSide1=int(input("Input side of rectangle: "))
    # rectangleSide2=int(input("Input height on to side of triangle:")
    s=rectangleSide1*rectangleSide2
    print("\nRectangle square is equal to ",s)
def circleSquare():
    """Function calculating circle square"""
    PI=3.14
    radius=int(input("Input radius of circle: "))
    s=PI*radius*radius
    print("\nCircle square is equal to ",s)
    
print("""
To find CircleSquare input:     c
To find rectangleSquare input:  r
To find triangleSquare input:   t
""")
userInput=input("Choose what calculating you need from the list above:")
if userInput:
    if userInput.lower()=="c":
        circleSquare()
    elif userInput.lower()=="r":
        rectangleSquare()
    elif userInput.lower()=="t":
        triangleSquare()
else:
    print("You inputed nothing. Try again")
#################################################################################################################
def numbersSum():
    """Function counting sum of all elements in number"""
    # number=input("Input some number: ")
    number=[int(i) for i in input("Input some number: ")]
    return print(sum(number))
numbersSum()
##############################################################################################################
def recursiveFibo(number):
    """Recursive function that building fibonachi sequence till number what user inputed"""
    if number <= 1:
       return number
    else:
       return(recursiveFibo(number-1) + recursiveFibo(number-2))

number=int(input("Input number: "))

if number <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence: ")
    for i in range(number):
        print(recursiveFibo(i),end=" ")
##############################################################################################################
def discriminant(a,b,c):
    """Function calculating discriminant of quadratic equation by formula in variable 'd'"""
    d=b*b-4*a*c
    return print("\nDiscriminant of quadratic equation is: ",d)

print("""We have equation a(x*x)+b(x)+c. 
Please input values for a,b,c to find 
discriminant of that equation below:\n""")

a=int(input("Input value of a: "))
b=int(input("Input value of b: "))
c=int(input("Input value of c: "))
discriminant(a,b,c)
