#!/usr/bin/env python
# TTL Logic Based Direct Digital Synthesis (DDS)
# 2021 TAPR/ARRL DCC Conference
# Mike McCann KB2GHZ

import sys
import operator
import math

# this function calculates the 2's complement of a byte value
def twoscomp(x):
   return (operator.xor((int(x) % 256),int(255))+1) % 256

def lsb(n):
   return n % 256

def msb(n):
   return (int(math.floor(n/256)))

reclen = 32  # default payload size
cnt = 0      # bytes in the current data record
cksum = 0
payload = ""
offset = 0   # address offset 
if len(sys.argv) != 3:
  print "Usage: IntelHex InputFile OutputFile"
  sys.exit()
inputFile = sys.argv[1]
outputFile = sys.argv[2]
input = open(inputFile)
output = open(outputFile, 'w')
for line in input:
  datum = int(line)
  hexVal = "%02X" % (int(datum))
  payload = payload + hexVal.upper()
  cksum = cksum + datum
  cnt = cnt + 1
  if cnt == reclen:
     output.write(":20")
     offsetStr = "%04X" % (offset)
     output.write(offsetStr)
     output.write("00")  # data record
     output.write(payload)
     cksum = cksum + lsb(cnt) + msb(cnt)
     cksum = cksum + lsb(offset) + msb(offset)
     check = "%02X" % (twoscomp(cksum))
     output.write(check)
     output.write("\r\n")
     offset = offset + reclen
     cnt = 0
     cksum = 0
     payload = ""
output.write(":")
len = "%02X" % (cnt)
output.write(len)
if cnt == 0:
   offset = 0
   cksum = 1
offsetStr = "%04X" % (offset)
output.write(offsetStr)
output.write("01")  # end of file record
output.write(payload)
check = "%02X" % (twoscomp(cksum))
output.write(check)
output.write("\r\n")



  
