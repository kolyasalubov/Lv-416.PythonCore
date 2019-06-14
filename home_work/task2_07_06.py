#You have to write a function that accepts three parameters:
#
#cap is the amount of people the bus can hold excluding the driver.
#on is the number of people on the bus.
#wait is the number of people waiting to get on to the bus.
#If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.


cap = int(input("Input amount of people the bus can hold: "))
on = int(input("Input number of people on the bus: "))
wait = int(input("Input the number of people waiting to get on to the bus: "))

def space_in_bus(cap, on, wait):
    return max(0, wait - (cap-on))
print(space_in_bus(cap, on, wait))








# def space_in_bus(cap, on, wait):
#     come_in =  (cap - on) - wait
#     if come_in < 0:
#         return -come_in
#     return 0
# print(space_in_bus(cap, on, wait))
