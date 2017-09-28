#!user/bin/env python
#-*- coding: utf-8 -*-

import csv
print 'h'
print 28 * 19
with open('./result.csv','r') as f:
    print "hello"
    cv = csv.reader(f)
    for line in cv:
        #if (len(line) != 28 * 19):
           # print "something goes wrong"
        print len(line)
