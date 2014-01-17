__author__ = 'german_or_jane'
import urllib.request
import smtplib

site = "http://itsupp.com/downloads/nod_update/"

def load(filename,site):
    myurl = site + filename

    with urllib.request.urlopen(myurl) as url:
     s = url.read()
    f = open("nod_update/"+filename, "wb")
    f.write(s)
    f.close()
    return "downloading done " + filename

def readupd(myurl):
    with urllib.request.urlopen(myurl) as url:
     s = url.read()
     print(len(s))

def parse(site):
    from lxml.html import parse
    # Получаем страничку
    logme = 'log of session'
    page = parse('http://itsupp.com/downloads/nod_update/').getroot()
    # Ищем все теги <a> с css классом topic
    hrefs = page.cssselect("a")
    for row in hrefs:
     # Получаем атрибут href
        exp = row.get("href")
        if exp[0] != '?' and exp[len(exp)-1] != '/':
            logme = logme + "\n" + load(exp,site)
    return logme
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
    return print('Ok')

mailtoadmin(parse(site))
