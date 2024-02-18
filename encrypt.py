#This program is completely untested. :)
from dictionary import characters as chars
from dictionary import colors as colormap

original_message = str(input('Enter the message you would like to encrypt into Lego bricks: '))
message = original_message
output = {'color': [], 'height': []}
error = False#4 testing
counter = 0#4 testing

def inChars(thing1):
    for color in colormap:
        if thing1 in chars[color]:
            return True
    return False

def get_bricks(thing2):
    return 

while len(message) > 0:
    couter += 1
    print(counter)
    charcom = len(message)
#    print('does ' + str(charcom) + "equal " + str(message[0:charcom]) + '?')
    print(message)
    while not inChars(message[0:charcom]):
        charcom = charcom - 1
        if charcom < 0:
            error = True
            print('OH NO error! :-(')
            exit()
        message = message[charcom:len(message)]
print('done!')
    