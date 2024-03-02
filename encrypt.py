from dictionary import characters as chars
from dictionary import colors as colormap

original_message = str(input('Enter the message you would like to encrypt into Lego bricks: '))
message = original_message
output = {'color': [], 'height': []}#take note of output format

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
    output['height'].append(chars[color].index(thing2))

def print_bricks(color, height):
    print('|' + str(color[0:3]) + '[ ]' * int((height - height % 3) / 3) + '|' * (height % 3) + str(height))

#the program must check message for compounds and characters. It does this by first checking if the entire message is a
#character/compound. If not, it checks if the whole message minus the last letter is a char/com. If not, it checks the whole
#message minus two letters. When it finds something that is in the chars list, it adds that to the output (in brick form) and
#removes that char/com from the front of message. Then it loops, and keeps going until message is empty.
while len(message) > 0:
    charcom = len(message)
    while not inChars(message[0:charcom]):
        charcom -= 1
        if charcom < 0:
            print('OH NO error! :-(')
            exit()
    get_bricks(message[0:charcom])#finds brick color and height, and adds those values to output
    message = message[charcom:len(message)]


print('Python array output:\n' + str(output) + '\nHere is your brick code:\n')
for stack in range(len(output['color'])):
    print_bricks(output['color'][stack], output['height'][stack] + 1)# +1 causes list to start at 1 instead of 0
print()