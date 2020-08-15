#!/usr/bin/python3
import urllib.request
import socket
import re

url = input('Input url - ')
host = re.findall("http[s]?://.+", url)
print(host[0])
fhand = urllib.request.urlopen(host[0])

total = 0
data = str()
for line in fhand:
    total = total + len(line.decode().strip())
    data = data + line.decode()

print(data[:3000])

print('\n----------\nTotal:{total}'.format(total=total))
