import sys
import os

def readfile(filename):
    f = open(filename, 'r')
    #print(f.read())
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
    f.close()

if __name__ == '__main__':
    readfile(input('input the filename: '))