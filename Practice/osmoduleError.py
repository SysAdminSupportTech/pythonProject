import os

try:
    filename = 'gfg.txt'
    f = open(filename, 'rU')
    text = f.read()
    f.close()
except IOError:
    print('Problem reading: ' + filename)