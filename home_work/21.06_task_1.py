"""Is the string uppercase?
Task
Create a method is_uppercase() to see whether the string is ALL CAPS. For example:"""


def is_uppercase(inp):
    if inp == inp.upper():
        return True
    else:
        return False