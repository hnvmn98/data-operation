import csv

rf = open('result.csv','r')
datareader = csv.reader(rf)

dataList = []
for rlist in datareader:
    dataList.append(rlist)
print(len(dataList))
num = range(1,58)
#1:Birth 2:Month 54:Type
index = []

for i in num:
    count = 0
    for dlist in dataList:
        if dlist[i-1] != '0':
            count += 1

    if count == 0:
        index.append(i-1)


print(index)

rf.close()
