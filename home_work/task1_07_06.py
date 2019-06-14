#You were camping with your friends far away from home, but when it's time to go back,
# you realize that you fuel is running out and the nearest pump is 50 miles away!
# You know that on average, your car runs on about 25 miles per gallon.
# There are 2 gallons left. Considering these factors, write a function that tells you if it is possible to get to the pump or not.
# Function should return true if it is possible and false if not.

distance = int(input("input distance in 'mile': "))
mpg = int(input("Input distance on 1 galone of your car: "))
galon = int(input("Input number of galons left: "))


def zero_fuel(distance_to_pump, mpg, fuel_left):
    if int(distance_to_pump) <= int(mpg) * int(fuel_left):
        return True
    else:
        return False
print(zero_fuel(distance, mpg, galon))