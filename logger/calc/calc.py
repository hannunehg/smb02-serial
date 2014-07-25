#!/usr/bin/python

from __future__ import division

#print((0x00 << 14) + (0x09 << 7) + 0x11)

f = open('reading.bin')
lines = f.readlines()
f.close()

#print "Reading, Value"
value = str(lines)

#print str(lines)
# === Voltage === #
index = value.find("01100000")
#print index

vData = value[index+8:] 
#print vData
value = value[66:] # trim voltage
#print value

v1 = vData[1:8]
#print v1
v2 =  vData[9:16]
#print v2
v3 = vData[17:24] 
#print v3

voltage = "%04d" % ((int(v1,2) << 14) + (int(v2,2) << 7) + int(v3,2))
#print voltage
#voltage = str(voltage)[0:2] + "." + str(voltage)[2:]# + " Volts"
#print "Voltage, " + voltage
print voltage


# === Current === #
index =  value.find("01100001")
#print index

cData = value[index+8:]
#print cData
value = value[66:] # trim current
#print value

cSign = cData[1:2]
#print cSign
c1 = cData[2:8]
#print c1
c2 =  cData[9:16]
#print c2
#print hex(int(c2,2))
c3 = cData[17:24]
#print hex(int(c3,2))

current = "%04d" % ((int(c1,2) << 14) + (int(c2,2) << 7) + int(c3,2))
#print current

if cSign == '0':
   current = current# str(current)[0:2] + "." + str(current)[2:]# + " Amps"
else:
   current = "-" + str(current) # str(current)[0:2] + "." + str(current)[2:]# + " Amps"

#print "Current, " + current
print current
#print str(bin(int(current)))[2:3]

# === Amphours === #

index =  value.find("01100010")
#print index

aData = value[index+8:]
#print aData
value = value[66:] # trim Amphours
#print value

aSign = aData[1:2]
#print aSign
a1 = aData[2:8]
#print a1
a2 =  aData[9:16]
#print a2
#print hex(int(a2,2))
a3 = aData[17:24]
#print a3

amphours = "%04d" % ((int(a1,2) << 14) + (int(a2,2) << 7) + int(a3,2))
#print amphours

if aSign == '0':
   amphours = amphours # str(amphours)[0:3] + "." + str(amphours)[3:]# + " Amphours"
else:
   amphours = "-" + str(amphours) # str(amphours)[0:3] + "." + str(amphours)[3:]# + " Amphours"

#print "Amphours, " + amphours
print amphours


# === state of charge === #

index = value.find("01100100")
#print index

pData = value[index+8:]
#print pData
value = value[66:] # trim state of charge
#print value

p1 = pData[1:8]
#print p1
p2 =  pData[9:16]
#print p2
p3 = pData[17:24]
#print p3

percentage = "%04d" % ((int(p1,2) << 14) + (int(p2,2) << 7) + int(p3,2) )
#percentage =  int(percentage) / 10

percentage = str(percentage)# + " %"
#print "State of Charge, " + percentage
print percentage


# === time to go === #

index =  value.find("01100101")
#print index

tData = value[index+8:]
#print tData
value = value[66:] # trim percentage
#print value

tSign = tData[1:2]
#print tSign
t1 = tData[2:8]
#print t1
t2 =  tData[9:16]
#print t2
#print hex(int(t2,2))
t3 = tData[17:24]
#print hex(int(t3,2))

time = ((int(t2,2) << 7) + int(t3,2))
#print time

if tSign == '0':
   #time = str(int(time/60)) + "h " + str(time%60) + "m"
   time = time 
#else:
#   time = -1 #"--- h"

#print "Time to Go, " + time
print time


# === temperature === #

index =  value.find("01100110")
#print index

teData = value[index+8:]
#print teData
value = value[66:] # trim time
#print value

teSign = teData[1:2]
#print teSign
te1 = teData[2:8]
#print te1
te2 =  teData[9:16]
#print te2
#print hex(int(te2,2))
te3 = teData[17:24]
#print hex(int(te3,2))

temp = "%03d" % ((int(te2,2) << 7) + int(te3,2))
#print temp

if teSign == '0':
   temp = temp # str(temp)[0:2] + "." + str(temp)[2:]# + " C"
else:
   temp = "-" + str(temp) #str(temp)[0:2] + "." + str(temp)[2:]# + " C"

#print "Temperature, " + temp
print temp



