#!user/bin/env python
#-*- coding: utf-8 -*-

import csv

with open('computeResult.csv','r') as f:
    cv = csv.reader(f)
    with open('finalResult.csv','a') as fr:
        for line in cv:
            if (len(line) == 1069):
                fr.write(','.join(line))
                fr.write('\n')

