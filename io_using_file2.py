import sys
import os

def readfile(filename):
    f = open(filename, 'r')
    print(f.read())
    f.close()

if __name__ == '__main__':
    readfile(input('input the filename: '))

