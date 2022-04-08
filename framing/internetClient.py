#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 17:41:39 2022

@author: general
"""

import socket, time, sys
sys.path.append('../../../../../Utep/lib')
import adclass

path = sys.argv[1]

socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
#host = socket.gethostname()
host = '127.0.0.1'

#regular port
#port = 50001

#stammer port
port = 50000

socketClient.connect((host, port))
handler = adclass.Archiver()

fileToSend = handler.fileToTransfer(path)
while True:
    
    while fileToSend:
        socketClient.send(fileToSend[:1024])
        fileToSend = fileToSend[1024:]
        
    break
print('file trasfered successfuly')
sys.exit(0)

