import socket
from datetime import datetime
from time import sleep

port = 10002
msg = "raspi[1] says " + "hello!"*30

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', port))

while True:
    data, (host, port) = s.recvfrom(4096)
    print data
    s.sendto(msg, (host, port))
