import csv
import random

rf = open('result-feiyan-selected.csv','r')
datareader = csv.reader(rf)
trainf = open('train.csv', 'w')
traindata = csv.writer(trainf)
testf = open('test.csv', 'w')
testdata = csv.writer(testf)

trainList1 = []
trainList2 = []
#trainList3 = []
#trainList4 = []
#trainList5 = []
#trainList8 = []


for rlist in datareader:
    l = []
    if (rlist[0] == '1'):
        l.append(1)
        for i in range(1,16):
            l.append(rlist[i])
        trainList1.append(l)
    else:
        l.append(0)
        for i in range(1,16):
            l.append(rlist[i])
        trainList2.append(l)
'''
    elif rlist[0] == '62':
        l.append(2)
        for i in range(1,57):
            l.append(rlist[i])
        trainList2.append(l)
    elif rlist[0] == '66':
        l.append(3)
        for i in range(1,57):
            l.append(rlist[i])
        trainList3.append(l)
'''
#    elif rlist[0] == '5':
#        trainList5.append(rlist)
#    elif rlist[0] == '8':
#        trainList8.append(rlist)

print(len(trainList1))
print(len(trainList2))
#print(len(trainList3))
#print(len(trainList4))
#print(len(trainList5))
#print(len(trainList8))

testList1 = random.sample(trainList1, int(round(len(trainList1) * 0.3)))
testList2 = random.sample(trainList2, int(round(len(trainList2) * 0.3)))
#testList3 = random.sample(trainList3, int(round(len(trainList3) * 0.3)))
#testList4 = random.sample(trainList4, int(round(len(trainList4) * 0.3)))
#testList5 = random.sample(trainList5, int(round(len(trainList5) * 0.3)))
#testList8 = random.sample(trainList8, int(round(len(trainList8) * 0.3)))
print(len(testList1))
print(len(testList2))
#print(len(testList3))
#print(len(testList4))

for m in testList1:
    trainList1.remove(m)
    testdata.writerow(m)
for m in testList2:
    trainList2.remove(m)
    testdata.writerow(m)
"""
for m in testList3:
    trainList3.remove(m)
    testdata.writerow(m)
for m in testList4:
    trainList4.remove(m)
    testdata.writerow(m)
"""

for n in trainList1:
    traindata.writerow(n)
for n in trainList2:
    traindata.writerow(n)
"""
for n in trainList3:
    traindata.writerow(n)
for n in trainList4:
    traindata.writerow(n)
"""

trainf.close()
testf.close()
