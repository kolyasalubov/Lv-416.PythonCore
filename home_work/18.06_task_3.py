"""Given a string, you have to return a string in which each character (case-sensitive) is repeated once."""


def double_char(s):
    res = ""
    for i in s:
        res += i * 2
    return str(res)

print(double_char("Hello World"))