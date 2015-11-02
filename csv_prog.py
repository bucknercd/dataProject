''' CSV PROGRAM'''
import csv, time

rpt1 = 'RptCareTCDetailNathanBonnet.csv'
rpt2 = 'RptCareTCDetailDanielKinney.csv'

fcr1 = 'FCRALLDetailReportNathanBonnet.csv'
fcr2 = 'FCRALLDetailReortMarissaLopez.csv'

f1 = open(rpt1, 'r')
csv_obj1 = csv.reader(f1)

accts = []

for row in csv_obj1:
   try:
      accts.append(row[10])
   except:
      print 'end of csv file'
f1.close()
accts.pop(0)

f2 = open('test.txt', 'w')
for i in accts:
   f2.write(i)
f2.close()

report = open('report.txt', 'a')

f2 = open(fcr2, 'r')
csv_obj2 = csv.reader(f2)
dic = {}

'''for row in csv_obj2:
   try:
      acct = row[7]
      name = row[3]
      dic[acct] = name
   except:
      print 'end of 2nd csv file'
      time.sleep(20)


for i in accts:
   info = dic[i]+'\t\t'+i'\n'
   report.write(info)'''
   


