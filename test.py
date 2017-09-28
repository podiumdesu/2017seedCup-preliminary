#!user/bin/env python
#-*- coding: utf-8 -*-

import csv
import os
os.remove('./result.csv')    #remove first
with open('teamData.csv','rb') as f:
    all_lines = len(f.readlines())
    print all_lines
with open('teamData.csv','rb') as f:
    f.readline()
    cv = csv.reader(f)
    flag = 1
    team = 0
    count = 2   #因为跳过了第一行
    # judge if it is last line
    for line in cv:     #line是个list
        with open('./result.csv', 'a') as fr:
            if (int(line[0]) == team):
                for x in line:
                    fr.write(x + ',')
                flag = flag + 1
                print flag
            else:

                #fr.write('now i need to add something')
                left = 28 - flag
                print left
                for i in range(0, left - 1):
                    for j in range(0, 19):
                        fr.write('0,')
                for j in range(0,18):
                    fr.write('0,')
                fr.write('0')

                fr.write('\n')
                for x in line:
                    fr.write(x + ',')
                flag = 2
                team = team + 1
            if (count == all_lines):

                left = 28 - flag
                print left
                for i in range(0, left - 1):   # for last '0'
                    for j in range(0, 19):
                        fr.write('0,')
                for j in range(0,18):
                    fr.write('0,')
                fr.write('0')

                fr.write('\n')
        count = count + 1
