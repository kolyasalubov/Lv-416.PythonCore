#Jenny has written a function that returns a greeting for a user.
# However, she's in love with Johnny, and would like to greet him slightly different. ' \
#        'She added a special case to her function, but she made a mistake.


name = input("Input your name: ")

def greeting_message(name):
    if  name == "Johny":
        return "Hello my Love"
    return "Hello {name}".format(name = name)

print(greeting_message(name))