#!/usr/bin/env python3


import os,sys

block = 16


def write(nameOfFile, array):
    tmp = os.open(nameOfFile, os.O_CREAT | os.O_WRONLY)
    os.write(tmp, array)


def  read(nameOfFile, size):
     # Returns a file decriptor for the os.read to read the file
     tmp = os.open(nameOfFile, os.O_RDONLY)
     return os.read(tmp, size)
 
def fileFactory(array):
    pass
    
        
def myEncode(string):
    arr = bytearray(block - len(string))
    for n in string:
        arr.append(ord(n))
    return arr



def myDecode(arr):
    n = ''
    for i in range(0, block):
        if arr[i] == 00:
            continue
        else:
            n += chr(arr[i])
            
    return n

def getFiles(path):
    tmp = os.listdir(path)
    files = {}
    total_size = 0
    for item in tmp:
        total_size += os.path.getsize(item)
        files[item] = os.path.getsize(item)
    
    return files, total_size


files, totalSize = getFiles('/Users/general/OneDrive/Utep/dummy')



def archive(files, totalSize):
    array = bytearray()
    ts = myEncode(str(totalSize))
    array += ts
    for name, size in files.items():
        n = myEncode(name)
        s = myEncode(str(size))
        f = read(name, size)
        array += n
        array += s
        array += f
        
        write('output.arch', array)
        
def openWholeFile(file):
    arr = bytearray()
    f = os.open(file, os.O_RDONLY)
    arr = os.read(f, 16)
    total = myDecode(arr)
    full = os.read(f, int(total))    
    return full


# archive(files, totalSize)


full = openWholeFile('output.arch')


