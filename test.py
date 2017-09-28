#!user/bin/env python
#-*- coding: utf-8 -*-

import csv
import os
os.remove('./result.csv')    #remove first
with open('test.csv','rb') as f:
    f.readline()
    cv = csv.reader(f)
    flag = 1
    team = 0
    for line in cv:     #line是个list
        with open('./result.csv', 'a') as fr:
            if (int(line[0]) == team):
                for x in line:
                    fr.write(x + ',')
                    flag = flag + 1
            else:
                left = 28 - flag
                for i in range(0, left):
                    fr.write('0,')
                fr.write('\n')
                for x in line:
                    fr.write(x + ',')
                flag = 1
                team = team + 1





