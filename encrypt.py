from dictionary import characters as chars
from dictionary import colors as colormap

#original_message = str(input('Enter the message you would like to encrypt into Lego bricks:'))
#message = original_message
error = False

def inChars(thing):
    for color in colormap:
        if thing in chars[color]:
            return True
    return False

"""
while message > 0:
    charcom = len(message)
    while not message[0:charcom] in chars:
        charcom = charcom - 1
        if charcom < 0:
            error = True
    
"""
print(inChars(''))