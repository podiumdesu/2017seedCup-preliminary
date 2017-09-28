#!user/bin/env python
#-*- coding: utf-8 -*-

import csv
print 'h'
print 27 * 19
with open('./result.csv','r') as f:
    print "hello"
    cv = csv.reader(f)
    for line in cv:
        print len(line)
        if (len(line) == 286):
            print line[285]
