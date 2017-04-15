#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import csv

file = open('olympic_dataset.csv')
intermediate_output1 = open('intermediate_output1.txt',"w")
csv_f=csv.reader(file)

for line in csv_f:
    sex = line[3]
    intermediate_output1.write("{0}\t{1}\n".format(sex, "1"))
intermediate_output1.close()

