import socket
from datetime import datetime
from time import sleep, time
import sys
import timeout_decorator

while True:
    s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    port = 10002

    #if sys.argv[1] == "uc":
        #host = sys.argv[2]

    if sys.argv[1] == "bc":
        s2.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s2.bind(('', 60001))
        host = "8.3.2.255"

    num_children = int(sys.argv[2])

    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    start = time()
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
