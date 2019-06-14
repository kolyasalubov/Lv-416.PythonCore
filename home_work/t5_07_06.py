#Consider an array of sheep where some sheep may be missing from their place.
# We need a function that counts the number of sheep present in the array (true means present).
lis = [True, True,True,False,False,True, True,True, True,False,False]

def count_sheeps(array_of_sheeps):
    return array_of_sheeps.count(True)

print(count_sheeps(lis))