__author__ = 'german_or_jane'
import smtplib

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

mailtoadmin('pppp')