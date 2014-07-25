#!/usr/bin/python

from __future__ import division
import math

f = open('reading.val')
lines = f.readlines()
f.close()

i = 0
for k in [1, 2, 3, 4, 5, 6]:

   v1 = int(str(lines[0+i:1+i])[2:-4],10)
   v2 = int(str(lines[6+i:7+i])[2:-4],10)
   v3 = int(str(lines[12+i:13+i])[2:-4],10)
   v4 = int(str(lines[18+i:19+i])[2:-4],10)
#   print str(v1) + " " + str(v2) + " " + str(v3) + " " + str(v4)

   vList = [v1,v2,v3,v4]
   
   for y in [1, 2, 3] :
   
      sum = 0
      j = 0
      for x in vList:
          sum = sum + vList[j]
          j = j+1
      #print sum
      mean = sum/j
      #print mean
      
      j = 0
      dVList = []
      for x in vList:
          dVList.append( math.fabs(vList[j] - mean) )
          j = j+1
      
      j = 0
      max = dVList[0] 
      maxIndex = 0
      #print max
      for x in dVList:
      
         if max < dVList[j]:
            max = dVList[j]
            maxIndex = j
         j = j+1
   
      #print max
      
   #   print vList
      del vList[maxIndex]
      #del dVList[maxIndex]
#      print vList
   
   i = i + 1
   print vList[0]


