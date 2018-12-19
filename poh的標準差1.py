#先複製寫入一次證券代碼至ROA稅前息前折舊前的資料
import xlrd, xlsxwriter, datetime
#D:\\Users\\USER\\Downloads\\VOL.xlsx
#D:\\Users\\USER\\Downloads\\hello123.xlsx 寫入檔案的excel
firm = "D:\\Users\\USER\\Downloads\\VOL.xlsx"

workbook = xlsxwriter.Workbook("D:\\Users\\USER\\Downloads\\VOL123.xlsx")#寫入一個新的excel
worksheet = workbook.add_worksheet()

fh1 = xlrd.open_workbook(firm)
sheet = fh1.sheet_by_index(0) #第一個工作表
    

def variance(return_list):     #用來求出標準差
  d_list = []
  for i in range(4):
    sqr = 0
    mean = sum(return_list[i:i+5]) / 5
    for j in range(5):
      sqr += (return_list[i + j] - mean) ** 2
    deviation = (sqr / 5) ** (1 / 2)
    d_list.append(deviation)
  return d_list

sec_dict = dict()

for row_index in range(1, 10911):
  
  try:
    sec_ID = (sheet.cell(row_index, 0).value)        #為了製作新的工作表
    sec_days = (sheet.cell(row_index, 1).value)      #用datetime轉為日期，若日期為9~12年則不寫入
    sec_return = (sheet.cell(row_index, 2).value)
    sec_roaa = (sheet.cell(row_index, 3).value)
    sec_roab = (sheet.cell(row_index, 4).value)
    sec_roac = (sheet.cell(row_index, 5).value)
    diff = datetime.timedelta(days = int(sec_days) - 2)
    y = datetime.datetime(1900, 1, 1)
    sec_date = y + diff
    sec_year = sec_date.strftime("%Y")
  except ValueError:
    continue

  
  if sec_ID not in sec_dict:                      #為了計算是否為8個完整年度
    number = 1
    sec_dict[sec_ID] = [1, [sheet.cell(row_index, 2).value], [sheet.cell(row_index, 3).value], [sec_date.strftime("%Y/%m/%d")], [sheet.cell(row_index, 4).value], [sheet.cell(row_index, 5).value]]

  elif sec_ID in sec_dict:

    sec_dict[sec_ID][0] += 1
    sec_dict[sec_ID][1].append(sheet.cell(row_index, 2).value)
    sec_dict[sec_ID][2].append(sheet.cell(row_index, 3).value)	
    sec_dict[sec_ID][3].append(sec_date.strftime("%Y/%m/%d"))
    sec_dict[sec_ID][4].append(sheet.cell(row_index, 4).value)
    sec_dict[sec_ID][5].append(sheet.cell(row_index, 5).value)
    #sec_dict[代碼]=[[有幾年],[報酬率],[roaa],[日期],[roab],[roac]]	
  
ID_list = list(sec_dict.keys())
ID_list.sort()

n = 1     #為了讓欄位累積
# print(ID_list)
for i in ID_list:
  if sec_dict[i][0] == 8:
    ret_ans = variance(sec_dict[i][1]) #報酬率標準差
    roa_ans = variance(sec_dict[i][2]) #roaa標準差
    # print(ret_ans)
	
    for k in range(len(ret_ans)):
      worksheet.write(n + k, 0, i)
      worksheet.write(n + k, 1, sec_dict[i][3][k]) #日期
      worksheet.write(n + k, 2, sec_dict[i][1][k]) #報酬率
      worksheet.write(n + k, 3, sec_dict[i][2][k]) #roaa
      worksheet.write(n + k, 4, sec_dict[i][4][k]) #roab
      worksheet.write(n + k, 5, sec_dict[i][5][k]) #roac
      worksheet.write(n + k, 6, ret_ans[k]) #報酬率標準差
      worksheet.write(n + k, 7, roa_ans[k]) #roaa標準差
    n += 4


workbook.close()
	
	