#!/usr/bin/python

import sys
sorted_op1 = open("sort01.txt","r")
sorted_op2 = open('sort02.txt',"r")
output01 = open("output01.txt","w")
output02 = open("output02.txt","w")
Total = 0
oldKey = None
countrykey = None
silver = 0
country = sorted_op2.readlines()
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



#######
for line1 in country:
    data = line1.strip().split("\t")
    if len(data) != 2:
        continue

    CountryKey, medals = data

    if countrykey and countrykey != CountryKey:
	if silver != 0:
         output02.write("{0}\t{1}\n".format(countrykey,silver)) 
        countrykey = CountryKey;
        silver = 0

    countrykey = CountryKey
    silver += int(medals)

if countrykey != None and silver != 0:
   output02.write(" {0}\t{1} \n".format(countrykey, silver)) 
output02.close()





