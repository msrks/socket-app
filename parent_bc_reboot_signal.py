#! -*- coding: utf-8 -*-
"""
usage:
$ python parent_bc_reboot_signal.py <dst-ip> <interval>
$ python parent_bc_reboot_signal.py 192.168.0.255 0.1
"""
import socket
from time import sleep
import sys

dst_ip = sys.argv[1] # "192.168.0.255"
dst_port = 10002
interval = float(sys.argv[2]) # 0.1

msg = b'\x00\x1a\x01\xe1\x0a\x0b\x0c\x0d\x0e\x0f\x00\x00\x09\x99\xe3\x00\x46\x55\x01\x00\x00\x00\x00\x00\x00\x01'

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.sendto(msg, (dst_ip, dst_port))
    sleep(interval)
