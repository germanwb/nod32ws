#!/usr/bin/python3
__author__ = 'german_or_jane'
import os
import datetime
import smtplib

import down
import unpack
import get_key

global txtmail
sistemname = 'Windows German Home'
date = datetime.datetime.now()
txtmail = sistemname+ " at " + date.strftime("%d/%m/%y %H:%M")+"\n"
def tomail(txt):
    global txtmail
    txtmail=txtmail+txt+"\n"
    print(txt)

def parse(name):
    f = open(name)
    classes = {}
    current_class = None
    for line in f.readlines():
        if line.startswith('['):
            current_class = line.strip('[]\n')
            classes[current_class] = {}
        else:

            st=line.rstrip()
            n=st.split('=')
            if len(n) == 2:
                classes[current_class].update({n[0]:n[1]})

    f.close()
    return classes



def check_dif():
    current = parse('base/update.ver')
    tomail(unpack.load_update())
    new_ver=parse('tmp/update.ver')
    auth = get_key.get_key()
    if auth == None:
        auth=['TRIAL-64582270','msfps6j264']
    for keys in new_ver.keys():
        if new_ver[keys].get('file'):
            if current.get(keys):
                if current[keys].get('file'):
                    if new_ver[keys].get('version') !=  current[keys].get('version'):
                        tomail(keys+':  '+current[keys].get('version')+"====>"+new_ver[keys].get('version'))
                        tomail(down.load_auth(new_ver[keys]['file'],auth))
                else:
                    if new_ver[keys].get('language'):
                        if new_ver[keys]['language'] == '1049':
                            tomail(down.load_auth(new_ver[keys]['file'],auth))
                            new_ver[keys]['file']=new_ver[keys]['file'].split('/')[-1]

                    else:
                        new_ver[keys]['file']=new_ver[keys]['file'].split('/')[-1]
                        tomail(down.load_auth(new_ver[keys]['file'],auth))
    return new_ver


def new_base():
    tomail(unpack.load_update())
    new_ver=parse('tmp/update.ver')
    auth = get_key.get_key()
    if auth == None:
        auth=['TRIAL-64582270','msfps6j264']
        tomail('use my key')
    for keys in new_ver.keys():
        if new_ver[keys].get('file'):
            if new_ver[keys].get('language'):
                if new_ver[keys]['language'] == '1049':
                    tomail(down.load_auth(new_ver[keys]['file'],auth))
                    new_ver[keys]['file']=new_ver[keys]['file'].split('/')[-1]
            else:
                tomail(down.load_auth(new_ver[keys]['file'],auth))
                new_ver[keys]['file']=new_ver[keys]['file'].split('/')[-1]
    return new_ver

def save_ver_file(new_ver):
    str=''
    for keys in new_ver.keys():
        str=str+'['+keys+"]\n"
        for values in new_ver[keys].keys():
            str = str+values+'='+new_ver[keys][values]+"\n"

    f = open("base/update.ver", "w")
    f.write(str)
    f.close()
    return 'all write'

def start():
    if os.path.exists('base/update.ver'):
        tomail('>>>start diff>>>')
        x = check_dif()
        save_ver_file(x)
        tomail(save_ver_file(x))

    else:
        tomail('generated new base>>>')
        x = new_base()
        save_ver_file(x)
        tomail(save_ver_file(x))
def mailtoadmin(msg):
    fromaddr = 'Germanlog White  <log@nzmi.info>'
    toaddr = 'Log Log <log@nzmi.info>'
    subj = 'my notification'
    msg_txt = 'Notice:\n\n ' +  msg + '\n\nBye!'
    msg = "From: %s\nTo: %s\nSubject: %s\n\n%s"  % ( fromaddr, toaddr, subj, msg_txt)
    username = 'log@nzmi.info'
    password = 'BuBuntu'
    server = smtplib.SMTP('smtp.yandex.ru:25')
    server.set_debuglevel(0);
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddr, msg)
    server.quit()

start()
print(txtmail)
#mailtoadmin(txtmail)
