"""
usage:
$ python parent_uc_exact_polling.py <dst-ip> <src-port> <interval>
$ python parent_uc_exact_polling.py 192.168.88.102 30003 0.1
"""
import socket
from datetime import datetime
from time import sleep, time
import sys
import timeout_decorator

dst_port = 10002
msg = "toooooooooooooooooooooth!"*12
len_payload = 68-14-20-8-4 # eth14 ip20 udp8 fcs4
msg = msg[:len_payload]

dst_ip = sys.argv[1] # "192.168.88.1"
src_port = int(sys.argv[2]) # 30003
interval = float(sys.argv[3]) # 0.1
timelimit = 0.9

while True:

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f")[:-3]

    s.bind(('', src_port))
    s.sendto(msg, (dst_ip, dst_port))
    start = time()

    @timeout_decorator.timeout(timelimit, timeout_exception=StopIteration)
    def rcv_packets():
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
