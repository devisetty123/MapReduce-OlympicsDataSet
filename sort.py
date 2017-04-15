#!/usr/bin/python
import sys
map_op1 = open("intermediate_output1.txt","r")
map_op2 = open("intermediate_output2.txt","r")
sort01 = open('sort01.txt',"w")
sort02 = open('sort02.txt',"w")
lines = map_op1.readlines()
countries = map_op2.readlines()
countries.sort()
lines.sort()
for line in lines:
	sort01.write(line)
for country in countries:
	sort02.write(country)
map_op1.close()
sort02.close()
map_op2.close()
sort01.close()
