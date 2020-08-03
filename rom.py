#!/usr/bin/env python
# TTL Logic Based Direct Digital Synthesis (DDS)
# 2020 TAPR/ARRL DCC Conference
# Mike McCann KB2GHZ

import math

def binStr(x):
  return format(x,'b').zfill(8)

ROMsize = 2**16
phaseDelta = 2 * math.pi / ROMsize
phase = 0.0

for i in range(ROMsize):
  signal = math.sin(phase)
  DAC = math.ceil(((signal + 1.0) * 127.5))
  binary = binStr(int(DAC))
  print "%i" % (i),
  print "\t%f" % (phase),
  print "\t%f" % (signal),
  print "\t%i" % (DAC),
  print "\t%02x" % (DAC),
  print
  phase = phase + phaseDelta



