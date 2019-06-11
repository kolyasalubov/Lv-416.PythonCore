#Your task is to complete this Class, the Person class has been created. 
# You must fill in the Constructor method to accept a name as string and an age as number, 
# complete the get Info property and getInfo method/Info getter which should return

class Person(object):
    info = ""
    def __init__(self, name,age):
        self.info = "{0}s age is {1}".format(name, age)
    def getInfo():
        return info