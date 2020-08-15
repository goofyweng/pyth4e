#!/usr/bin/python3
import socket
import re

url = input('Input url - ')
host = re.findall("http[s]?://(.+)/", url)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host[0], 80))

cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
mysock.send(cmd.encode())

total = 0
while True:
    data = mysock.recv(1000)
    if len(data) < 1:
        break

    total = total + len(data.decode())

    if total <=  3000:
        print(data.decode(),end='')
        print('\n>>Total number of characters displayed: {}'.format(total))

print('\n----------\nTotal number of characters in the file: {}'.format(total))
mysock.close()
