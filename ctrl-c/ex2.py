# ex3.py

import thread, win32api

def handler(sig, hook=thread.interrupt_main):
    hook()
    return 1

win32api.SetConsoleCtrlHandler(handler, 1)

import time

try:
    import arcpy
    while True:
        print "sleep ",
        time.sleep(2)
except KeyboardInterrupt:
    print "KeyboardInterrupt detected!"
