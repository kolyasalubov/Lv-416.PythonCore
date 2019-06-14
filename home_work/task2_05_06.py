#You need to write a function that reverses the words in a given string. A word can also fit an empty string. If this is not clear enough, here are some examples:

#As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.


#  variant 1

# stroka = "Hello awer beautiful world"
#
# def revers_string(stringa):
#     stringa = " ".join( stroka.split(" ")[::-1] )
#     return stringa
#
# print(revers_string(stroka))
#

# variant 2

def reverse(st):
    st = st.split()
    st.reverse()
    st = " ".join(st)
    return st

print(reverse("Hello awer beautiful world"))