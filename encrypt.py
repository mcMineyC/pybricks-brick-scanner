#This program is completely untested. :)
from dictionary import characters as chars
from dictionary import colors as colormap

original_message = str(input('Enter the message you would like to encrypt into Lego bricks: '))
message = original_message
output = {'color': [], 'height': []}
counter = 0#var is 4 testing purposes only

def inChars(thing1):
    global chars, colormap
    for color in colormap:
        if thing1 in chars[color]:
            return True
    return False

def get_bricks(thing2):
    global chars, colormap
    for color in colormap:
        if thing2 in chars[color]:
            break
    output['color'].append(color)
    output['height'].append(chars[color].index(thing2) + 1)#note the + 1



#the program must check message for compounds and characters. It does this by first checking if the entire message is a
#character/compound. If not, it checks if the whole message minus the last letter is a char/com. If not, it checks the whole
#message minus two letters. When it finds something that is in the chars list, it adds that to the output (in brick form) and
#removes that char/com from the front of message. Then it loops, and keeps going until message is empty.
while len(message) > 0:
    counter += 1
    print('counter == ' + str(counter))
    charcom = len(message)
    while not inChars(message[0:charcom]):
        charcom -= 1
        if charcom < 0:
            print('OH NO error! :-(')
            exit()
    get_bricks(message[0:charcom])#finds brick color and height, and assigns those values to output
    message = message[charcom:len(message)]
print('done!')
print('output == ' + str(output))