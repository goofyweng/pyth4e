import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        address = 'http://py4e-data.dr-chuck.net/comments_42.xml'

    parms = dict()
    parms['address'] = address
    print('Retrieving', parms['address'])
    uh = urllib.request.urlopen(parms['address'],context = ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    # print(data.decode())
    tree = ET.fromstring(data)
    counts = tree.findall('.//count')
    # print(counts[0].text, type(counts[0].text))
    print('Counts:',len(counts))
    # print('Counts[0]', type(counts[0]))

    # counts is a list of  xml.etree.ElementTree.Element
    # use Element.text to get the value of the element
    sum = 0
    for count in counts:
        sum += int(count.text)
        # print(count.text)
    print('Sum:', sum)
