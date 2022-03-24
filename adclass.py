#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 21:34:48 2022

@author: general
"""
import os

class Archiver:
    


    def write(self, nameOfFile, array):
        tmp = os.open(nameOfFile, os.O_CREAT | os.O_WRONLY)
        os.write(tmp, array)
    
    
    def  read(self, nameOfFile, size):
         # Returns a file decriptor for the os.read to read the file
         tmp = os.open(nameOfFile, os.O_RDONLY)
         return os.read(tmp, size)
    
    

    def fileToTransfer(self, path):
        fileToSend = bytearray()
        root, name = os.path.split(path)
        fileToSend = self.prepArray(path, name)
        
        return fileToSend
    
    
    def archive(self, path, name='archived.pff'):
        fileToWrite = bytearray()
        
        if path[-1:] == '/':
            for root, dirs, files in os.walk(path, topdown=False):
                for file in files:
                    fullPath = os.path.join(root, file)
                    fileToWrite += self.prepArray(fullPath, file)
            
            self.write(name, fileToWrite)
                    
        else:
            print(f'{path} is no a folder')
        

            
    def deArchive(self, file='archived.pff'):
        # total =  length of file to be recreated
        total = os.path.getsize(file)
        # full read the entire file
        full = self.read(file, total)
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
            info = full[:size]; self.write(name, info); full = full[size:]
            
        os.remove('archived.pff')
        
    
    def prepArray(self, fullPath, file):
        # create a byte array
        array = bytearray()
        # add the lenght of the file name
        array += (f'{len(file):02d}'.encode())
        # add the actual file name
        array += (f'{file}'.encode())
        # add the length of the file size
        array += (f'{os.path.getsize(fullPath):08d}'.encode())
        # add the actual file
        array += (self.read(fullPath, os.path.getsize(fullPath)))
            
        # return the complete array (can be many files added to this array)
    
        return array
