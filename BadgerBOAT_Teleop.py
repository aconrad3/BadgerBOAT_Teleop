#from getkey import getkey, keys
#key = getkey()
#
#buffer = 0
#
#while 1:
#    if key == keys.UP:
#    # Handle the UP key
#        print("Butts")
#    elif key == keys.DOWN:
#        print("Butts2")
#    # Handle the DOWN key
#    # Handle all other desired control keys
#    else:  # Handle text characters
#      buffer += key
#      print(key)
#
#
#
#
#

from __future__ import print_function
import sys, select, termios, tty
import time
import serial

def getKey():

        tty.setraw(sys.stdin.fileno())
        select.select([sys.stdin], [], [], 0)
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        return key
#with serial.Serial('/dev/ttyACM0', 115200, timeout=1) as ser :
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
while 1:

    settings = termios.tcgetattr(sys.stdin)
    key = getKey()
    if key == 'q':
         print("Quitting Teleop!")
         
         sys.exit(1)
    elif key == 'w':
        ser.write(bytes('W\n'))
        #time.sleep(.1)
    elif key == 's':
        ser.write(bytes('S\n'))
       # time.sleep(.1)
    elif key == 'a':
        ser.write(bytes('A\n'))
    elif key == 'd':
        ser.write(bytes('D\n'))
    else:
        ser.write(bytes('Z\n'))
    print(key)

      


