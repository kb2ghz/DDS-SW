#!/usr/bin/env python
# TTL Logic Based Direct Digital Synthesis (DDS)
# 2020 TAPR/ARRL DCC Conference
# Mike McCann KB2GHZ

import math
import sys

if len(sys.argv) != 2 :
   sys.exit()

freq = float(sys.argv[1])

# 100 KHz clock, 16 bit phase accumulator
fclk=100000.0
n=16

deltaF = fclk/(2**n)
tw = freq/deltaF

print "Tuning Word Value = 0x%04x" % math.floor(tw)

