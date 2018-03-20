#!/usr/bin/env python

import commands
import os

def blkid():
  result = []
  out = commands.getoutput('sudo blkid | grep -v sdb')
  lines = out.splitlines()
  for line in lines:
     if 'dev/sd' in line:
         index = line.rfind('=', 0, 40)
         param = line[index + 2:53]
     result.append(param)
  return result
print(blkid())
