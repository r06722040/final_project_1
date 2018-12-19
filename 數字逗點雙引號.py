csv = input()
start = 0
end = 0

for i in range(len(csv)):
  start = end #記住起點(為上筆資料的結尾)
  if csv[i] == "\"" and i not in range(0, end): #找出第一個引號的位置(避免抓到夾在中間的雙引號)
    start = i
    for next in range(start + 1, len(csv)):
      if csv[next] == "\"":                     #next 為下一個雙引號的位置
        end = next + 2        #end為下個資料的起點
        break
    print(csv[start:end - 1]) #start為第一個引號， end - 1 為資料結尾的逗點
  
  elif csv[i] == "," and i not in range(0, end): #end 為下筆資料起點之所在位置
    end = i + 1
    print(csv[start:end - 1])
print(csv[end:])  #印出最後一筆資料
