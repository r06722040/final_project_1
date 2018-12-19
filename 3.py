data = []
count = 0
comp = set((input()).split(', '))
print(type(comp))
# comp for compare, 利用list(set(<list>))去除重複值

# 讀取檔案
while True:
    a = input()
    if a == '_END_':
        break
    if len(a) > 1:
        count += 1
        data.append([set(a.split(', ')), count])

for item in data:
    item[0] = len(item[0].intersection(comp)) / len(item[0].union(comp))

data.sort(key=lambda i: i[0], reverse=True)    
# 根據每個list的第一個element做 reversed 排序
for i in data:
    print(i[1], '%.4f' % i[0])