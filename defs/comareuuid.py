#!/usr/bin/env python

import commands
import os

def blkid():
  result = []
  out = commands.getoutput('sudo blkid | grep -v sdb')
  lines = out.splitlines()
  for line in lines:
     if 'dev/sd' in line:
         #print line
         index = line.rfind('UUID=')
         #print index
         param = line[index + 6: index + 42]
     result.append(param)
  return result
#print(blkid())

def fstauuid():
  result = []
  fh = open('/etc/fstab')
  for line in fh:
    # in python 2
      if not line.startswith('#') and line.strip():
         index = line.rfind('=', 0, 40)
       #print index
         param = line[index + 1:41]
         result.append(param)
 #return result
    #   print type(line.split())
     #print type(line)
    # in python 3
    #print(line)
  fh.close()
  return result
#print type(fstauuid())
#print(fstauuid()) 
#For i in fstauuid() :
#  for j in blkid() :
#    if i != j :
#      print i
#
#
for i in fstauuid() :
  if i not in blkid():
    print i 
#for fstabuuid() in blkid () :
  #print fstabuuid()
