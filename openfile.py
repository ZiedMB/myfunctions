
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


print(fstauuid())
