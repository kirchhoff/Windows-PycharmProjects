#coding=utf-8
from socket import *
HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = raw_input(">")
    print "data is ",data
    if not data:
        break
    tcpCliSock.send('%s\n' % data)
    data = tcpCliSock.recv(BUFSIZE)
    print 'data is ', data
    if not data:
        break
    print data.strip()
    tcpCliSock.close()