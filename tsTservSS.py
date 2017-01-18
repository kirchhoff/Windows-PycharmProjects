#coding=utf-8
from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime
from socket import *
HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print "...connected from:", self.client_address
        self.wfile.write('[%s] %s' % (ctime(),self.rfile.readline()))
        print "send successful"

tcpServ = TCP(ADDR, MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()
# tcpServer = socket(AF_INET, SOCK_STREAM)
# tcpServer.bind(ADDR)
# tcpServer.listen(5)
#
# while True:
#     print 'waiting for connection...'
#     sockclient, addr = tcpServer.accept()
#     print "addr is ",addr
#     data = sockclient.recv(1024)
#     print 'data is ',data
#     sockclient.send('%s' % ctime())
#     sockclient.close()
