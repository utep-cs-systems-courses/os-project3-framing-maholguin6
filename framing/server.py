#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 17:34:37 2022

@author: general
"""

import socket, sys, time, os
import adclass as handler


#create a socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# host machine
#host = socket.gethostname()
host = '127.0.0.1'
port = 50001

# bind to the port

serverSocket.bind((host, port))
serverSocket.listen(10)
serverHandler = handler.Archiver()
file = bytearray()

while True:
    
    clientSocket, addr = serverSocket.accept()
    print(f'address: {addr}')
    if os.fork() == 0:
        
        t = clientSocket.recv(1024)
        while t:
            print(f'length of t: {len(t)}')
            file += t
            print(f'length of size: {len(file)}')
            t = clientSocket.recv(1024)
        serverHandler.fileReceived(file)
    clientSocket.shutdown(socket.SHUT_WR)
    
serverSocket.close()
    
        