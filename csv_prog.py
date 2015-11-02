''' CSV PROGRAM'''
import csv, time

rpt1 = 'RptCareTCDetailNathanBonnet.csv'
rpt2 = 'RptCareTCDetailDanielKinney.csv'

fcr1 = 'FCRALLDetailReportNathanBonnet.csv'
fcr2 = 'FCRALLDetailReortMarissaLopez.csv'
r = csv.reader(open(rpt1,'r'))
items = []
next(r, None)
for row in r:
   items.append(row[10])

print items
time.sleep(2)
f = open('test.txt', 'w')
f.write(items)

