from pynput import keyboard
import serial

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
print("BadgerBOAT Teleop Command Begin!")

def on_press(key):
    try: k = key.char # single-char keys
    except: k = key.name # other keys
    if key == keyboard.Key.esc:
        ser.write('z'.encode())

        return False # stop listener
    if k =='w': # keys interested
        
        ser.write('w'.encode())
       # time.sleep(.005)
    if k == 'a':
        ser.write('a'.encode())
       # time.sleep(.005)
    if k == 's':
        ser.write('s'.encode())
        #time.sleep(.005)
    if k == 'd':
        ser.write('d'.encode())
        #time.sleep(.005)
        


def on_release(key):
    try: k = key.char # single-char keys
    except: k = key.name # other keys
    if key == keyboard.Key.esc: return False # stop listener
    ser.write('z'.encode())
    #if k in ['w', 'a', 's', 'd']: # keys interested
        # self.keys.append(k) # store it in global-like variable
    print('Key released: ' + k)
    if key == keyboard.Key.esc:
        # Stop listener
        ser.write('z'.encode())

        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


