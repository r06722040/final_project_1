class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    #計算x,y與原點之距離平方
    def magnitude(self):   
        mag = (self.x) ** 2 + (self.y) ** 2
        return mag
    #self跟某p比大小
    def isSmallerThan(self, p):
        if self.magnitude() < p.magnitude():
            return True
        else:
            return False

n = int(input())
xlist = input().split()
ylist = input().split()

for i in range(n):               #將xlist,ylist之元素轉為int
    xlist[i] = int(xlist[i])
    ylist[i] = int(ylist[i])

anslist = []
for i in range(n):              #創建一個1,2,3,.....,n的list
    anslist.append(i+1)

for i in range(n-1):        #每一圈能多確定一項為最大值，故做n-1圈就得排序完畢
    for j in range(n-1-i):    #每做完一圈就多確定後面數來一項，故圈數減少
        now = Point(xlist[j],ylist[j])          #賦予目前編號跟下一編號x及y
        nextp = Point(xlist[j+1],ylist[j+1])
        if now.isSmallerThan(nextp) == False:   #若now與原點的距離不小於nextp
            anslist[j],anslist[j+1] = anslist[j+1],anslist[j]  #將anslist中之兩項之順序交換
            xlist[j],xlist[j+1] = xlist[j+1],xlist[j]          #同時調整xlist,ylist中的順序
            ylist[j],ylist[j+1] = ylist[j+1],ylist[j]

for i in range(len(anslist)):
    if i != len(anslist)-1:
        print(anslist[i],end = " ")
    else:
        print(anslist[i])
