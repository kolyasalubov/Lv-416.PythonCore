#Create a function which answers the question "Are you playing banjo?".
#If your name starts with the letter "R" or lower case "r", you are playing banjo!

def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        name = name + " plays banjo"
    else:
        name = name + " does not play banjo"
    return name