#!/usr/bin/python3
import socket
import re

url = input('Input url - ')
host = re.findall("http[s]?://(.+)/", url)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host[0], 80))

cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
mysock.send(cmd.encode())

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
    print('\nlength: ', len(data.decode()), '\n')

mysock.close()
