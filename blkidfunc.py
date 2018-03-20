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
print(blkid())
