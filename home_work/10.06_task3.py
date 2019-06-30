"""Write a function taking in a string like WOW this is REALLY amazing and returning Wow this is really amazing. String should be capitalized and properly spaced. Using re and string is not allowed.

Examples:

filter_words('HELLO CAN YOU HEAR ME') #=> Hello can you hear me
filter_words('now THIS is REALLY interesting') #=> Now this is really interesting
filter_words('THAT was EXTRAORDINARY!') #=> That was extraordinary! """


def filter_words(st):
    st = st.lower()
    st_splited = st.split()
    st = ' '.join(st_splited)
    print(st[0].upper() + st[1:])
    return st[0].upper() + st[1:]


filter_words("HELLO CAN YOU HEAR ME")