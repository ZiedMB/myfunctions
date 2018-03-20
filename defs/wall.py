import os
#for file in os.listdir("/mydir"):

import sys                                           
for file in os.listdir("/dev/pts/"):
 with open("/dev/pts/"+file, "wb+", buffering=0) as term:
    term.write("hello".encode())
#def wallit(msg):
#for file in os.listdir("/dev/pts/"):
#  print file
