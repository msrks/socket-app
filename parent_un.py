import socket
from datetime import datetime
from time import sleep, time
import sys
import timeout_decorator


s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
num_children = int(sys.argv[1])

host_name = ['8.3.1.2','8.3.1.24','8.3.1.40','8.3.1.56','8.3.1.72','8.3.1.88',
             '8.3.1.104','8.3.1.108','8.3.1.120','8.3.1.145','8.3.1.195',
             '8.3.1.196','8.3.1.191','8.3.1.174','8.3.1.173','8.3.1.128',]

for host in host_name:
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    start = time()
    port = 10002
    s2.sendto("tooooooooooooooooooooooooooooooooooooth!"*8, (host, port))

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    port = 30000
    s.bind(('', port))

@timeout_decorator.timeout(5)
def rcv_packets():
    for i in range(num_children):
        r = s.recv(4096)
        stop = time()
        print now, r[:9], round(stop-start, 3), "s"

try:
    rcv_packets()
except:
    print "timeout!!!!!"
    print ""
else:
    print ""
