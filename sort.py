#!/usr/bin/python
import sys
map_op1 = open("intermediate_output1.txt","r")
sort01 = open('sort01.txt',"w")
lines = map_op1.readlines()
countries = map_op2.readlines()
countries.sort()
lines.sort()
for line in lines:
	sort01.write(line)
map_op1.close()
sort01.close()
