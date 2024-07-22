#!/bin/python3
from ev3dev2.motor import Motor, OUTPUT_D, OUTPUT_C
from ev3dev2.led import Leds
from ev3dev2.sensor.lego import TouchSensor, ColorSensor
from ev3dev2.sensor import INPUT_3, INPUT_4
from ev3dev2.button import Button
from dictionary import characters as chars
from dictionary import colors as colormap
from translate import translate
import time, math
#from random import randint #Used for testing while actual implementation not complete

def move_studs(studs):
    global drivetrain
    drivetrain.on_for_degrees(-100, (studs*260))

def get_degrees_touchy():
    global touchy
    pos = touchy.position * (360 / touchy.count_per_rot)
    return pos


drivetrain = Motor(address=OUTPUT_D)
touchy = Motor(address=OUTPUT_C)
toucher = TouchSensor(address=INPUT_4)
color_sensor = ColorSensor(address=INPUT_3)


print() #clean up via \n when you get the chance.
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
print("(Re)Init touchy motor")
input("Press any key to continue.")
touchy.on_for_rotations(100, -10)
print("Resetting touchy position")
touchy.position = 0
print("Moving 1 stud")
move_studs(1)
print("Done initing.")
md = [] #Master dict
count = 0
go = True
vals = []
while (go):
    vd = dict() #Current stack dict
    deg = 0

    #Wait for 0 degrees
    # print("Waiting for 0 degrees, current: "+str(get_degrees_touchy()))
    if(get_degrees_touchy() > 10):
        touchy.on(-75)                                         #Turn motor on backward (up)
        while (get_degrees_touchy() > 10):
            # print("Degrees is not 0: "+str(get_degrees_touchy()))
            time.sleep(0.05)
        touchy.stop()
        time.sleep(2)
        # print("Degrees is "+str(get_degrees_touchy()))
        touchy.position = 0
    
    move_studs(1)
    time.sleep(1)
    touchy.on(75)                                              #Turn motor on forward (down)
    while not (toucher.is_pressed == 1):
        # print("Not touched, "+str(get_degrees_touchy()))
        if (get_degrees_touchy() > 2900):
            go = False
            break
        time.sleep(0.1)
    touchy.stop()                               #Stop motor
    time.sleep(2)
    if not go:
        print("EXITING!!!!")
        go = False
        touchy.stop()
        break
    color = color_sensor.color_name.lower()    #Capture color
    deg = get_degrees_touchy()
    print("Degrees "+str(deg))
    v = deg
    height = deg

    if deg is not None:                                         #Check if valid
        touchy.position_sp = 0                                  #Reset
        touchy.run_to_abs_pos()                                 #Go? IDK why it takes two lines

    #Store values in dict, using string keys for readability
    vd['color'] = color
    vd['height'] = height
    brickicks = (((math.floor((height-163)/90))*-1)+30-8 if ((((height-163)/90))*-1)+30-8 < math.floor((height-163)/90)+0.5 else (math.ceil(((height-163)/90))*-1)+30-8)
    vd["brickicks"] = brickicks
    print("step 0 "+str((height-163)/90))
    print("step 1 "+str(round((height-163)/90)*-1))
    print("step 1.33 "+str(brickicks)
    print("step a "+str(math.floor((height-163)/90)))
    print("Inverted " +str(math.floor((height-163)/90)*-1))
    print("adjusted "+str((math.floor((height-163)/90)*-1)+30))
    print("Saving bricks "+str((((1 if ((math.floor((height-163)/90)*-1)+30) < 0 else math.floor((height-163)/90)))*-1)+30))
    md.append(vd)
    count+=1
print("Done reading.\n"+str(md))
concat_str = ""
end = int(input("Enter number of bricks to translate (1 to " + str(len(md)) + "): "))
if end > len(md) or end < 0:
    end = len(md)
    print("Invalid input, using max value of " + str(end))

for c in range(end):  #Ignore last one because it's gonna be 29.  -1 for list index
    concat_str += translate(md[c]['color'], md[c]['brickicks'])
print("|               Done!                 |")
print("|\t\t" + concat_str + "\t\t|")
print("|        Thank you and goodbye!       |")
print("+-------------------------------------+")
