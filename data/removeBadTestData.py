#!user/bin/env python
#-*- coding: utf-8 -*-


import csv
import os

os.remove('finalTestResult.csv')
with open('computeTestResult.csv','r') as f:
    cv = csv.reader(f)
    with open('finalTestResult.csv','a') as fr:
        for line in cv:
            print len(line)
            if (len(line) == 1012):
                fr.write(','.join(line))
                print 'hello'
                fr.write('\n')

