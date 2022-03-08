from pynput.keyboard import Key, Controller

keyboard = Controller()
#Press and release space
keyboard.press(Key.space)
keyboard.release(Key.space)


keyboard.press('A')
keyboard.release('A')
while keyboard.pressed(Key.shift):
    keyboard.press('a')
    keyboard.release('a')

    #Print message
    keyboard.type("Hello World")