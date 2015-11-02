''' CSV PROGRAM'''
import csv, time

rpt1 = 'RptCareTCDetailNathanBonnet.csv'
rpt2 = 'RptCareTCDetailDanielKinney.csv'

fcr1 = 'FCRALLDetailReportNathanBonnet.csv'
fcr2 = 'FCRALLDetailReortMarissaLopez.csv'

f1 = open(rpt1, 'r')
csv_obj = csv.reader(f1)

accts = []

for row in csv_obj:
   try:
      accts.append(row[10])
   except:
      print 'end of csv file'
f1.close()
f2 = open('test.txt', 'w')
for i in accts:
   f2.write(i)
f2.close()

report = open('report.txt', 'w')

f2 = open(fcr2, 'r')
csv_obj = csv.reader(f2)

for row in csv_obj:
   try:
      acct_num = row[7]
      name = row[3]
   except:
      print 'end of 2nd csv file'
   if acct_num in accts:
      info = name +'\t'+acct_num
      report.write(info)


