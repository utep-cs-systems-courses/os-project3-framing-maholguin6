#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 17:34:37 2022

@author: general
"""

import socket, sys, time, os, threading
sys.path.append('../../../../../Utep/lib')
import adclass

#create a socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# host machine
#host = socket.gethostname()
host = '127.0.0.1'
port = 50001

# bind to the port

def reciver(clientSocket):
    file = bytearray()
    t = clientSocket.recv(1024)
    while t:
        print(f'length of t: {len(t)}')
        file += t
        print(f'length of size: {len(file)}')
        t = clientSocket.recv(1024)
    serverHandler.fileReceived(file)


serverSocket.bind((host, port))
serverSocket.listen(10)
serverHandler = adclass.Archiver()

while True:
    
    clientSocket, addr = serverSocket.accept()
    print(f'address: {addr}')
        
    t1 = threading.Thread(target=reciver, args=(clientSocket,))
    
    t1.start()
    t1.join()
    clientSocket.shutdown(socket.SHUT_WR)
    
serverSocket.close()
    
        