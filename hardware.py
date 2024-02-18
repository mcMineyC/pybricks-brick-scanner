#!/bin/python3
from ev3dev2.motor import Motor, OUTPUT_D, OUTPUT_C
from ev3dev2.led import Leds
from ev3dev2.sensor.lego import TouchSensor, ColorSensor
from ev3dev2.sensor import INPUT_3, INPUT_4
from ev3dev2.button import Button
import utils
from dictionary import characters as chars
from dictionary import colors as colormap
from translate import translate
import time
#from random import randint #Used for testing while actual implementation not complete


"""
#Setup multiprocessing for faster operation
#Multiprocessing return values
pool = ThreadPool(processes=1)

async_result = pool.apply_async(foo, ('world', 'foo')) # tuple of args for foo

# do some other stuff in the main process

return_val = async_result.get()  # get the return value from your function.
"""


vals = None
drivetrain = None
touchy = None
toucher = None
color_sensor = None

def move_studs(studs):
    global drivetrain
    drivetrain.on_for_degrees(-100, (studs*259))

def get_degrees_touchy():
    global touchy
    pos = touchy.position * (360 / touchy.count_per_rot)
    return pos

def quickInit():
    global drivetrain
    global touchy
    global toucher
    global color_sensor
    drivetrain = Motor(address=OUTPUT_D)
    touchy = Motor(address=OUTPUT_C)
    toucher = TouchSensor(address=INPUT_4)
    color_sensor = ColorSensor(address=INPUT_3)

def init():
    touchyInit()
    return True

def touchyInit():
    global touchy
    print("(Re)Init touchy motor")
    input("Press any key to continue.")
    touchy.on_for_rotations(100, -10)
    touchy.position = 0



def getValues():
    global touchy
    global toucher
    md = dict() #Master dict
    count = 0
    go = True
    while (go):
        vd = dict() #Current stack dict
        deg = 0
        #Wait for 0 degrees
        while (get_degrees_touchy() > 10):
            print("Degrees is not 0: "+str(get_degrees_touchy()))
            time.sleep(0.1)
        print("Degrees is 0")
        touchy.on(100)                                              #Turn motor on forward (down)
        while not (toucher.is_pressed == 1):
            print("Not touched")
            if (get_degrees_touchy() > 2900):
                go = False
                break
            time.sleep(0.1)
        if not go:
            print("EXITING!!!!")
            go = False
            touchy.stop()
            break
        color = color_sensor.color_name    #Capture color
        touchy.stop()                      #Stop motor
        deg = get_degrees_touchy()
        print("Degrees "+str(deg))
        v = deg
        if deg is not None:                                         #Check if valid
            touchy.position_sp = 0                                  #Reset
            touchy.run_to_abs_pos()                                 #Go? IDK why it takes two lines
        height = deg

        #Store values in dict, using string keys for readability
        vd['color'] = color
        vd['height'] = height
        md[count] = vd
        count+=1
        move_studs(1)
    print("Done reading.\n"+str(md))
    return md


#Main script
def main():
    quickInit()
    async_init = init()
    move_studs(1)
    if(not async_init):
        print("Error initing.")
        return
    print("Done initing.")
    vals = getValues()
    concat_str = ""
    for c in vals:
        concat_str += translate(vals[c]['color'], vals[c]['height'])
    print("|               Done!                 |")
    print("|\t\t" + concat_str + "\t\t|")
    print("|        Thank you and goodbye!       |")
    print("+-------------------------------------+")




print()
print()
print("+-------------------------------------+")
print("|         THE EPIC LEGO READER        |")
print("|          BY JEDI AND CONNOR         |")
print("+-------------------------------------+")
print()
print()
print("              Starting...             ")
print()
print()
main()