value_int=10
value_float=8.4
value_str="No"
big_int=value_int*3.5
value_float-=1
value_str=value_str*2+"Yes"*3
value_int/value_float
big_int/value_float
print(f"""
           Results
.=============================.
| value_str   = {value_str} |
| value_float = {value_float}           |
| big_int     = {big_int}          |
| value_int   = {value_int}            |
'============================='             """)
print("value_int/value_float = ",value_int/value_float)
print("big_int/value_float   = ",big_int/value_float)
