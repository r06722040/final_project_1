class Time:
  def IsBetween(self, start, end):   #辨認時間是否在起始與結束之間
    start_total = start.hour * 3600 + start.minute * 60 + start.second
    end_total = end.hour * 3600 + end.minute * 60 + end.second
    self_total = self.hour * 3600 + self.minute * 60 + self.second
    if end_total >= self_total >= start_total:
      return True
    else:
      return False
		
  Doubledigit = True
  def ToString(self):
    if Time.Doubledigit == True:  #處理兩位數補零
      TimeString = "0" + str(self.hour) + ":" if self.hour < 10 else str(self.hour) + ":"
      TimeString += "0" + str(self.minute) + ":" if 0 <= self.minute < 10 else str(self.minute) + ":"	  
      TimeString += "0" + str(self.second) if 0 <= self.second < 10 else str(self.second) 
    return TimeString
	
def theT(thetime):  #將時間分成 小時，分鐘，分秒的屬性
  t = Time()
  hour, minute, second = thetime.split(":")
  t.hour = int(hour)
  t.minute = int(minute)
  t.second = int(second)
  return t

def TospltList(thelist): #將csv資料分成各個字串
  theL = thelist[0].split(",")
  return theL


import csv
ans = "D:\\Users\\USER\\Downloads\\midterm2.csv"

fh1 = open(ans, "r", newline = "")
cheader = fh1.readline()
reader1 = csv.reader(fh1, delimiter = "\t")  #叫出學生一筆資料，辨認時間是否在輸入裏頭
Startup = theT(input()) #hh:mm:ss 輸入開始時間
Endup = theT(input())   #hh:mm:ss 輸入結束時間
PSList = []
for data in reader1:
  thedatatime = theT(TospltList(data)[6])  #將所有時間叫出來，使其符合至開始結束。
  if thedatatime.IsBetween(Startup, Endup) == True:
    PSList.append(TospltList(data)[2:4])

for ps in PSList:  #將題目編號轉成整數
  ps[0] = int(ps[0])
 
for number in range(1, 5):
  problem = []
  AC = 0
  CE = 0
  RE = 0
  TLE = 0
  WA = 0
  for ps in PSList:
    if ps[0] == number:
      AC += ps.count("Accepted")
      CE += ps.count("Compile Error")
      RE += ps.count("Runtime Error")
      TLE += ps.count("Time Limit Exceed")
      WA += ps.count("Wrong Answer")
  print(str(AC) + " " + str(CE) + " " + str(RE) + " " + str(TLE) + " " + str(WA) + ";", end = "")
print()
fh1.close()
