#!/usr/bin/python

import sys
sorted_op1 = open("sort01.txt","r")
output01 = open("output01.txt","w")
Total = 0
oldKey = None
lines = sorted_op1.readlines()
for line in lines:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, count = data_mapped

    if oldKey and oldKey != thisKey:
        output01.write("{0}\t{1}\n".format(oldKey, Total)) 
        oldKey = thisKey;
        Total = 0

    oldKey = thisKey
    Total += int(count)

if oldKey != None:
   output01.write("{0}\t{1} \n".format(oldKey, Total)) 
output01.close()
sorted_op1.close()




