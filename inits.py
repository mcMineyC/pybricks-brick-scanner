import utils
@utils.threaded
def init():
    touchyInit()
    return True

def touchyInit():
    global touchy
    print("(Re)Init touchy motor")
    touchy.on_for_rotations(100, -10)
    touchy.position = 0