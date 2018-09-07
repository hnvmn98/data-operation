# -*- coding:utf-8 -*-
import csv
import datetime

rf = open('test.csv','r')
datareader = csv.reader(rf)
wf = open('result.csv', 'w')
datawriter = csv.writer(wf)

lastid = ''
i = 0
wlist = []
for rlist in datareader:
    wlist = []
    date = datetime.datetime.strptime(str(rlist[0]), "%Y/%m/%d")
    wlist.append(date.month)
    for i in range(1,58):
        wlist.append(rlist[i])
    datawriter.writerow(wlist)
datawriter.writerow(wlist)
rf.close()
wf.close()
