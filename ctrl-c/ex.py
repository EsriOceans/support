import arcgisscripting
import signal
import time

def ctrlc(sig, frame):
    raise KeyboardInterrupt("CTRL-C!")

print "Waiting..."
time.sleep(2)
print "Installing SIGINT handler"
signal.signal(signal.SIGINT, ctrlc)

try:
    while(True):
        print "sleep ",
except KeyboardInterrupt:
    print "KeyboardInterrupt detected!"
