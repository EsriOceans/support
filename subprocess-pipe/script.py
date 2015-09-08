import sys
import os

log = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'script.log')
with open(log, 'w') as f:
    for arg in sys.argv:
        print(arg)
        f.write("{}\n".format(arg))
