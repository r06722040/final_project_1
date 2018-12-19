a,b = input().split()
a,b = int(a),int(b)

datalist = []
for i in range(a):
    datalist.append(input().split())

#print(datalist)

for i in range(len(datalist)):
    for j in range(len(datalist[i])):
        datalist[i][j] = int(datalist[i][j])

p0 = []

for i in range(a):  #for迴圈
    p0.append(datalist[i][0])

dic = dict()
count = 1

for i in range(1,b+1):
    sum = 0
    for j in range(a):
        sum += (datalist[j][i] - p0[j]) ** 2
    dic[count] = sum
    count += 1
#print(dic)
dicrev = dict()

for key in dic:
    if dic[key] not in dicrev:
        dicrev[dic[key]] = [key]
    else:
        dicrev[dic[key]].append(key)
    
#print(dicrev)
anslist = sorted(dicrev)
printans = []

for key in anslist:
    for i in sorted(dicrev[key],reverse = True):
        printans.append(i)
    
for i in range(len(printans)):
    if i != len(printans)-1:
        print(printans[i],end = " ")
    else:
        print(printans[i])