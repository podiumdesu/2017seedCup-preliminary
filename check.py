#!user/bin/env python
#-*- coding: utf-8 -*-

import csv
print 'h'

with open('./test.csv','r') as f:
    print "hello"
    f.readline()
    cv = csv.reader(f)
    for line in cv:
        if (0 == int(line[0])):
            print "yes"
        print len(line)
        print line[0]
        print type(line[0])