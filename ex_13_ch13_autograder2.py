import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        address = 'http://py4e-data.dr-chuck.net/comments_42.json'

    parms = dict()
    parms['address'] = address
    print('Retrieving', parms['address'])
    uh = urllib.request.urlopen(parms['address'],context = ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js:
        print('=====Failure To Retrieve=====')
        continue

    # print(json.dumps(js, indent = 4))
    # js is a dictionary
    # js['comments'] is a list
    print('Count:', len(js['comments']))
    sum = 0
    for comment in js['comments']:
        sum += comment['count']

    print('Sum:', sum)
