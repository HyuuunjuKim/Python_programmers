scissor = '가위'
rock = '바위'
paper = '보'

win = '이김'
draw = '비김'
lose = '짐'

"""
mine = '가위'
yours = '바위'

if mine == yours :
    result = draw
else:
    result = '이기거나 지거나'

print(result)
"""

# else+if -> elif

mine = '가위'
yours = '바위'
if mine == yours :
    result = draw
else :
    if mine == scissor :
        if yours == rock :
            result = lose
        else :
            result = win
    elif mine == rock :
            if yours == paper :
                result = lose
            else :
                result = win
    elif mine == paper :
            if yours == scissor :
                result = lose
            else :
                result = win
print(result)