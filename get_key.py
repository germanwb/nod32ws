#!/usr/bin/python3
__author__ = 'german_or_jane'
def get_key_nodkeysru():
    import feedparser
    rss_url = "http://trial-nod32-keys.ru/news/rss"
    feed = feedparser.parse(rss_url)
    page = feed['entries'][0]['summary_detail']['value']
    page = page.replace('</div>',' ')
    page = page.replace('<div...',' ')
    page = page.replace(' ','')
    auth = {}
    n = page.split('<br>')
    i=0
    for m in n:
        x = m.split('<div>')
        auth[i] = {}
        for y in x:
            if y != '':
                xx=y.split(':')
                auth[i].update({xx[0]:xx[1]})
        i = i+1
    return auth

def validkey(username,password):
    from urllib.request import Request, urlopen
    from base64 import b64encode
    from urllib import error
    url = 'http://update.eset.com/v3-rel-bat/mod_000_loader/em000_64_l0.nup'
    request = Request(url)
    auth = b64encode(bytes(username + ":" + password, "ascii")).decode("ascii")
    request.add_header("Authorization", "Basic %s" % auth)
    allok = True
    try:
        response = urlopen(request)
    except error.HTTPError as err:
        allok = False
    return allok
def get_key():
    auth = get_key_nodkeysru()
    for m in auth.keys():
        if validkey(auth[m]['Username'],auth[m]['Password']):
            valid_auth=[auth[m]['Username'],auth[m]['Password']]
            return valid_auth

x=['TRIAL-64582270','msfps6j264']
validkey(x[0],x[1])