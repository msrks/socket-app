import socket
from datetime import datetime
from time import sleep

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    port = 10002
    s.bind(('', port))
    data, (host, port) = s.recvfrom(4096)
    print data

    s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    port = 30000
    msg = "raspi[1] says " + "hello!"*30
    s2.sendto(msg, (host, port))
