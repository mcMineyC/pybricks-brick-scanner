from dictionary import characters as chars
from dictionary import colors as colormap
import math
from random import randrange

def translate(color, height):
    bricks = math.floor((height-163)/90) #Inverted
    height = (bricks*(-1))+30       #Corrected with a max of 30
    color_name = color
    string = str(chars[color_name][height-1])
    print(color_name + "\t" + str(height) + "\t\t" + string)
    return string


"""
#Testing
concatstr = ""
for x in range(0,31):
    print(str(x)+ ":\t", end="")
    concatstr += " " + translate(randrange(0,6), 163+(90*x))

print("\n\n"+concatstr)
"""