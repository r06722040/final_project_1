import csv, datetime
def printans(dic):
        if "Accepted" in dic:
            print(dic['Accepted'],end=" ")
        else:
            print(0,end=" ")
        if "Compile Error" in dic:
            print(dic['Compile Error'],end=" ")
        else:
            print(0,end=" ")
        if "Runtime Error" in dic:
            print(dic['Runtime Error'],end=" ")
        else:
            print(0,end=" ")
        if "Time Limit Exceed" in dic:
            print(dic["Time Limit Exceed"],end=" ")
        else:
            print(0,end=" ")
        if "Wrong Answer" in dic:
            print(dic['Wrong Answer'],end=";")
        else:
            print(0,end=";")

class submission:
    def putin(a,info):
        a.submissionID = info[0]
        a.stuedentID = info[1]
        a.problem = info[2]
        a.status = info[3]
        a.score = info[4]
        a.codelenth = info[5]
        a.time = info[6]
        return a
 
    def isvalidtime(self,a,b):
        infosec = self.time.split(":")
        asec = a.split(":")
        bsec = b.split(":")
        self.time = int(infosec[0]) * 3600 + int(infosec[1]) * 60 + int(infosec[2])
        atime = int(asec[0]) * 3600 + int(asec[1]) * 60 + int(asec[2])
        btime = int(bsec[0]) * 3600 + int(bsec[1]) * 60 + int(bsec[2])
        if self.time >= atime and self.time <= btime:
            return True
        else:
            return False

    def process(self,onedic):
        if self.status not in onedic:
            onedic[self.status] = 1 
        else:
            onedic[self.status] += 1
        return onedic
       

        
start,end = input().split()

fn1 = "/Users/hsiao/Documents/碩二上/python/mid.csv"
fh1 = open(fn1, 'r', newline = '', encoding = 'utf-8')
csv1 = csv.DictReader(fh1)
cname1 = csv1.fieldnames
p1 = dict()
p2 = dict()
p3 = dict()
p4 = dict()

student_info_list=[]

for aline in csv1:
    student_info_list.append([aline[cname1[0]],aline[cname1[1]],aline[cname1[2]],aline[cname1[3]],aline[cname1[4]],aline[cname1[5]],aline[cname1[6]]])


for each in student_info_list:
    tem = submission()
    tem = tem.putin(each)
    #print(tem.status)
    if tem.isvalidtime(start,end) == True:
        if tem.problem == "1":
            tem.process(p1)
        if tem.problem == "2":
            tem.process(p2)
        if tem.problem == "3":
            tem.process(p3)
        if tem.problem == "4":
            tem.process(p4)


printans(p1)
printans(p2)
printans(p3)
printans(p4)
  
fh1.close()


#sudo python /Users/hsiao/Documents/碩二上/python/cousera3_1.py
