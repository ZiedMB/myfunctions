#!/usr/bin/env python

import commands
import os

out = commands.getoutput('sudo blkid | grep -v sdb')
lines = out.splitlines()
for line in lines:
     #print line
     if 'dev/sd' in line:
         index = line.rfind('=', 0, 40)
         param = line[index + 2:53]
         print param
