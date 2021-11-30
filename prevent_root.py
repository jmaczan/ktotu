from os import path
from constants import rootPath
from sys import exit

def prevent_root():
    userPath = path.expanduser('~')
    if(userPath == rootPath):
        print('Please run ktotu as not root.')
        exit()