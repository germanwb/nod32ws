#!/usr/bin/python3

__author__ = 'german_or_jane'


#serv = 'update.eset.com'
#username = 'TRIAL-0102806073-2'
#password = 'kk436d6tmj'
#file='/v3-rel-bat/mod_017_translator/em017_32_l1.nup'

def load_auth(file,authkey):
    from urllib.request import Request, urlopen
    from base64 import b64encode
    from urllib import error
    url = 'http://update.eset.com'+file
    n=file.split('/')
    file=n[-1]
    request = Request(url)
    auth = b64encode(bytes(authkey[0] + ":" + authkey[1], "ascii")).decode("ascii")
    request.add_header("Authorization", "Basic %s" % auth)
    allok = True
    try:
        response = urlopen(request)
    except error.HTTPError as err:
        allok=False
        return str(err.code)

    if allok == True:
        s = response.read()
        f = open("base/"+file, "wb")
        f.write(s)
        f.close()
    return file+'==>Ok'
