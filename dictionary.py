
colors = ('black', 'blue', 'green', 'yellow', 'red', 'white', 'brown')

characters = {
'black': [' ', 's', 'm', 'v', 'T', 'R', 'F', 'J', '3', '.', ';', '*', '/', 'ñ', 'í', '¿', 'Connor', 'has', 'had', 'come', 'think', 'show', 'read', 'found', 'saw', 'got', 'eat', 'really', 'Joshua', 'cool'], 
'blue': ['e', 'h', 'w', 'k', 'A', 'D', 'G', 'X', '4', '!', '-', '&', '<', '|', 'ó', '¡', 'Jedidiah', 'look', 'were', 'made', 'say', 'set', 'need', 'learn', 'turn', 'run', 'watch', 'ing', 'Norah', 'not'], 
'green': ['t', 'r', 'f', 'j', 'O', 'L', 'Y', 'Q', '5', '?', '_', '^', '>', "\\", 'õ', '~', 'Mullarky', 'see', 'write', 'can', 'may', 'help', 'put', 'move', 'should', 'might', 'walk', 'let', 'ed', 'good'], 
'yellow': ['a', 'd', 'g', 'x', 'I', 'C', 'P', 'Z', '6', ',', '=', '%', '[', 'ń', 'ú', '`', 'McClimans', 'will', 'could', 'said', 'take', 'tell', 'does', 'try', 'add', 'close', 'began', 'cut', 'are'], 
'red': ['o', 'l', 'y', 'q', 'N', 'U', 'B', '0', '7', "'", '+', '$', ']', 'á', '√', 'you', 'would', 'been', 'use', 'know', 'follow', 'must', 'change', 'keep', 'seem', 'took', 'talk', 'totally', 'Joel', "'s", 'great'], 
'white': ['i', 'c', 'p', 'z', 'S', 'M', 'V', '1', '8', '"', '(', '#', '{', 'ã', 'π', 'make', 'call', 'did', 'live', 'came', 'ask', 'play', 'start', 'open', 'hear', 'being', 'why', 'Braden', '. ', 'code'], 
'brown': ['n', 'u', 'b', 'E', 'H', 'W', 'K', '2', '9', ':', ')', '@', '}', 'é', '®', 'like', 'find', 'get', 'give', 'want', 'went', 'spell', 'thought', 'begin', 'stop', 'miss', 'leave', 'Jace', 'very', 'supercalifragilisticexpialidocious']}

state = False
print(len(characters))
for var in colors:
    print(var + ' ' + str(len(characters[var])))
    if "are" in characters[var]:
        state = True


print("WORD IS IN LISTS:"+str(state))