#!/bin/python

import sys
import socket
from datetime import datetime

target =  sys.argv[1]
print("-" * 50)
print("Scanning target "+ target) 
print("Time started: " + str(datetime.now()))
print("-" * 50)
try:    
    for port in range(50,86):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port is open {}".format(port))
        s.close()
        print(port,"Scanned ")

except KeyboardInterrupt:
    print("\nExiting Program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to a server.")
    sys.exit()
