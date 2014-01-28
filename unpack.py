#!/usr/bin/python3

__author__ = 'german_or_jane'
import os
import urllib.request
import sys
def load_update():
    with urllib.request.urlopen('http://update.eset.com/eset_upd/update.ver') as url:
     s = url.read()
    f = open("tmp/update.rar", "wb")
    f.write(s)
    f.close()
    mydir = os.getcwd()
    os.chdir(os.getcwd()+'/tmp')
    if sys.platform == "win32":
        print('Try')
        os.system('UnRar.exe x update.rar -o+ -inul')
        print('Ok')
    elif sys.platform == "linux2":
        os.system('unrar x update.rar -o+ -inul')
    else:
        os.system('./unrar x update.rar -o+ -inul')
    os.chdir(mydir)
    return 'unpack OK'

