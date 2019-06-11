#HELP! Jason can't find his textbook! It is two days before the test date, and Jason's textbooks 
#are all out of order! Help him sort a list (ArrayList in java) full of textbooks by subject,
#so he can study before the test.

#The sorting should NOT be case sensitive

def sorter(textbooks):
    less = []
    equal = []
    greater = []

    if len(textbooks) > 1:
        pivot = textbooks[0]
        for val in textbooks:
            if val.upper() < pivot.upper():
                less.append(val)
            elif val.upper() == pivot.upper():
                equal.append(val)
            elif val.upper() > pivot.upper():
                greater.append(val)
        return sorter(less)+equal+sorter(greater)
    else:
        return textbooks