#Given a string, you have to return a string in which 
#each character (case-sensitive) is repeated once.

def double_char(s):
    result = ''
    for val in s:
        result += 2*val
    return result