#!/usr/bin/python

from __future__ import division
import datetime


f = open('res')
lines = f.readlines()
f.close()


#print "Time, Voltage, Current, Amphours, State of Charge, Time to Go, Temperature"

volt = int(str(lines[0:1])[2:-4],10)
curr = int(str(lines[1:2])[2:-4],10)
amphours = int(str(lines[2:3])[2:-4],10)
percentage = int(str(lines[3:4])[2:-4],10)
time = int(str(lines[4:5])[2:-4],10)
temp = str(lines[5:6])[2:-4]

#print str(volt) + " " + str(curr) + " " + str(amphours) + " " + str(percentage) + " " + str(time) + " " + str(temp)


# === Voltage === #
volt = str(volt)[0:2] + "." + str(volt)[2:] + " Volts" 

# === Current === #
if curr > 0:
   curr =  str(curr)[0:2] + "." + str(curr)[2:] + " Amps"
else:
   curr =  str(curr)[0:3] + "." + str(curr)[3:] + " Amps"

# === Amphours === #
if amphours > 0:
   amphours = str(amphours)[0:3] + "." + str(amphours)[3:] + " Amphours"
else:
    amphours = str(amphours)[0:4] + "." + str(amphours)[4:] + " Amphours"

# === state of charge === #
percentage = str(percentage/10) + " %"

# === time to go === #
if time > 0:
   time = str(int(time/60)) + "h " + str(time%60) + "m"
else:
   time = "--- h"

# === temperature === #
if temp[0:1] != "-" :
   temp =  str(temp)[0:2] + "." + str(temp)[2:] + " C"
else:
   temp = str(temp)[0:3] + "." + str(temp)[3:] + " C"


print  str(datetime.datetime.now()) + ", " + str(volt) + ", " + str(curr) + ", " + str(amphours) + ", " + str(percentage) + ", " + str(time) + ", " + str(temp)




