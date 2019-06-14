#Create a function which answers the question "Are you playing banjo?".
#If your name starts with the letter "R" or lower case "r", you are playing banjo!
#
#The function takes a name as its only argument, and returns one of the following strings:


name = input("Input your name: ")

def areYouPlayingBanjo(name):
    if name.lower().startswith("r"):
        return "{} plays banjo".format(name)
    return "{} does not play banjo".format(name)

print(areYouPlayingBanjo(name))






# def banjo(name):
#     name = name.lower()
#     if name.startswith("r"):
#         return "{} plays banjo!".format(name)
#     else:
#         return "{} does not play banjo!".format(name)
# print(banjo(name))