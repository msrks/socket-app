import socket
import subprocess

src_port = 10002

cmd = 'cat /etc/dhcpcd.conf | grep ip_address=192 | cut -d "." -f4 | cut -d "/" -f1'
_id = subprocess.check_output(cmd, shell=True)
id = _id[1:-1]
msg = "raspi[" + id + "] says " + "hello!"*30
#len_payload = 100-14-20-8-4 # eth14 ip20 udp8 fcs4
len_payload = 84-14-20-8-4 # eth14 ip20 udp8 fcs4
msg = msg[:len_payload]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', src_port))

while True:
    data, (host, port) = s.recvfrom(4096)
    #print data
    s.sendto(msg, (host, port))
