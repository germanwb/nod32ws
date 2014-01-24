#!/usr/bin/python3

__author__ = 'german_or_jane'
import os
import urllib.request
def load_update():
    with urllib.request.urlopen('http://update.eset.com/eset_upd/update.ver') as url:
     s = url.read()
    f = open("tmp/update.rar", "wb")
    f.write(s)
    f.close()
    mydir = os.getcwd()
    os.chdir(os.getcwd()+'/tmp')
    os.system('./unrar x update.rar -o+ -inul')
    os.chdir(mydir)
    return 'unpack OK'
