#In this game, there are 21 sticks lying in a pile. Players take turns taking 1, 2, or 3 sticks. 
# The last person to take a stick wins.

def make_move(sticks):
    return max(sticks % 4, 1)