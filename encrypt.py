#This program is completely untested. :)
from dictionary import characters as chars
from dictionary import colors as colormap

original_message = str(input('Enter the message you would like to encrypt into Lego bricks:'))
message = original_message
error = False

def inChars(thing):
    for color in colormap:
        if thing in chars[color]:
            return True
    return False

while message > 0:
    charcom = len(message)
    print('does ' + str(charcom) + "equal " + str(message[0:charcom]) + '?')

    while not inChars(message[0:charcom]):
        charcom = charcom - 1
        if charcom < 0:
            error = True
    