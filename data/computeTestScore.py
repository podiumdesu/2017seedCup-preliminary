#!user/bin/env python
#-*- coding: utf-8 -*-

import csv
import re
import os

os.remove('computeTestResult.csv');
team = list(range(0,277))
with open('result.csv','r') as data:
    data_cv = csv.reader(data)
    count = 0
    for line in data_cv:
        team[count] = ','.join(line)
        print team[count]
        count = count + 1

with open('matchDataTest.csv','r') as f:
    f.readline()

    cv = csv.reader(f)
    with open('computeTestResult.csv','a') as fr:
        for line in cv:
            fr.write(team[int(line[0])] + ',');
            fr.write(team[int(line[1])] + ',');
            score_guest = re.findall(r"\d+\.?\d*",line[2]);
            score_host = re.findall(r"\d+\.?\d*",line[3]);
            fr.write(score_guest[0] +',')
            fr.write(score_guest[1]+',')
            fr.write(score_host[0]+',')
            fr.write(score_host[1])
            fr.write('\n')




