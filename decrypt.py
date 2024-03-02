from dictionary import characters as chars
from dictionary import colors as colormap

#set daInput to the desired dict array and run.
daInput = {'color': ['blue', 'blue', 'blue', 'black', 'yellow', 'green', 'black', 'blue', 'red', 'green', 'blue', 'black', 'blue', 'black', 'blue', 'black', 'yellow', 'white', 'blue', 'black', 'blue', 'blue'], 'height': [17, 9, 9, 0, 4, 0, 0, 2, 0, 1, 3, 1, 9, 0, 4, 2, 0, 3, 16, 0, 7, 5]}
daOutput = ''
def decode(input_array):
    global daOutput
    for brick in range(len(input_array['color'])):
        daOutput = daOutput + chars[input_array['color'][brick]][input_array['height'][brick]]
    return daOutput

print('Here is your decrypted message:\n' + decode(daInput))