import sys
import os

def readfile(filename):
    f = open(filename, 'r')
    print(f.read())
    f.close()

if __name__ == '__main__':
    file='poem.txt'
    readfile(file)

