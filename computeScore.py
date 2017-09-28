#!user/bin/env python
#-*- coding: utf-8 -*-

import csv
import re
import os

os.remove('computeResult.csv');
team = list(range(0,277))
with open('result.csv','r') as data:
    data_cv = csv.reader(data)
    count = 0
    for line in data_cv:
        team[count] = ','.join(line)
        print team[count]
        count = count + 1

with open('matchDataTrain.csv','r') as f:
    f.readline()

    cv = csv.reader(f)
    with open('computeResult.csv','a') as fr:
        for line in cv:
            fr.write(team[int(line[0])] + ',');
            fr.write(team[int(line[1])] + ',');
            score_guest = re.findall(r"\d+\.?\d*",line[2]);
            score_host = re.findall(r"\d+\.?\d*",line[3]);
            score_match = re.findall(r"\d+\.?\d*",line[4]);
            fr.write(score_guest[0] +',')
            fr.write(score_guest[1]+',')
            fr.write(score_host[0]+',')
            fr.write(score_host[1]+',')
            print score_match[0]
            print score_match[1]
            if (int(score_match[0]) > int(score_match[1])):
                print "客"
                fr.write('1');
            else:
                fr.write('0');
            fr.write('\n')
            print team[0]




