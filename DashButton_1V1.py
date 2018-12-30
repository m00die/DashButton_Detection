#!/usr/bin/python3

import time
import os
import signal
import socket




ip = "192.168.100.87"
x = 0
y = 0

while True:
    os.system("ping -c 1 " + ip)
    if os.system("ping -c 1 " + ip) == 0:

        if (x < 1):

            y = 0
            print ("Dash Button Ein")

            UDP_IP = "192.168.100.77" #.77 Loxone
            UDP_PORT = 2345
            MESSAGE = "DashEin"
                
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
            x = 1

                
    else:
        if (y < 1):

            x = 0
            print ("Dash Button Aus")

            UDP_IP = "192.168.100.77" #.77 Loxone
            UDP_PORT = 2345
            MESSAGE = "DashAus"
                
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
            y = 1
                
    # time.sleep(1)
