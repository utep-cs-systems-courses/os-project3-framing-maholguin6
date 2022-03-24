#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 22:46:43 2022

@author: general
"""
import os

arch = 'archived.pff'

def write(nameOfFile, array):
    tmp = os.open(nameOfFile, os.O_CREAT | os.O_WRONLY)
    os.write(tmp, array)
    
    
def  read(nameOfFile, size):
     tmp = os.open(nameOfFile, os.O_RDONLY)
     return os.read(tmp, size)
    
        
def archive(path, name=arch):
    fileToWrite = bytearray()  
    for root, dirs, files in os.walk(path, topdown=False):
        for file in files:
            fullPath = os.path.join(root, file)
            fileToWrite += prep(fullPath, file)

    write(name, fileToWrite)

def fileTransfer(path):
    root, name = os.path.split(path)
    toSend = prep(path, name)
    write(name, toSend)
    
    
def prep(fullPath, file):
    array = bytearray()
    array += (f'{len(file):02d}'.encode())
    array += (f'{file}'.encode())
    array += (f'{os.path.getsize(fullPath):08d}'.encode())
    array += (read(fullPath, os.path.getsize(fullPath)))
        
    return array

def deArchive(file=arch):
    # total =  length of file to be recreated
    total = os.path.getsize(file)
    # full read the entire file
    full = read(file, total)
    # two bytes reserved for the length of the name ex. (file.txt = 8 bytes )
    nameOffset = 2
    # eight bytes reserved for the length of the size
    sizeOffset = 8
    while full:
        # trim the two bytes of the name length off the file
        nameSize = int(full[:nameOffset].decode()); full = full[nameOffset:]
        # trim the length of the actual size of the file name to be created.
        name = full[:nameSize].decode();            full = full[nameSize:]
        # trimm off the size of the file
        size = int(full[:sizeOffset].decode());     full = full[sizeOffset:]
        # trim the actual file lenght
        info = full[:size]; write(name, info); full = full[size:]
        
    os.remove(arch)
    
    
   
def main():
    
    path = input('Please enter the path:')
    if path[-1:] == '/':
        archive(path)
                
    else:
        print('make sure the path ends with /')
    
    deArchive(arch)
    
main()


