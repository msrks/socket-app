"""
usage:
$ python parent_bc_exact_polling.py <dst-ip> <num-child> <interval>
$ python parent_bc_exact_polling.py 192.168.88.255 16 0.1
"""
import socket
from datetime import datetime
from time import sleep, time
import sys
import timeout_decorator

src_port = 30000
dst_port = 10002
msg = "toooooooooooooooooooooth!"*12
len_payload = 68
msg = msg[:len_payload]

dst_ip = sys.argv[1] # "192.168.88.255"
num_children = int(sys.argv[2]) # 16
interval = float(sys.argv[3]) # 0.1
timelimit = 0.9

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f")[:-3]

    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.bind(('', src_port))
    s.sendto(msg, (dst_ip, dst_port))
    start = time()

    @timeout_decorator.timeout(timelimit, timeout_exception=StopIteration)
    def rcv_packets():
        for i in range(num_children):
            r = s.recv(4096)
            stop = time()
            print now, r[:9], round(stop-start, 3), "s"

    try:
        rcv_packets()
    except StopIteration:
        print "timeout!!!!!"
    finally:
        print ""
        response_time = time() - start
        sleeptime = interval - response_time
        sleep(sleeptime)
