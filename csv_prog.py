
import csv, time

rpt_list = []
fcr_list = []

rpt_list.append('RptCareTCDetailNathanBonnet.csv')
rpt_list.append('RptCareTCDetailDanielKinney.csv')

fcr_list.append('FCRALLDetailReportNathanBonnet.csv')
fcr_list.append('FCRALLDetailReportMarissaLopez.csv')

accts = []

def create_acct_keys(file_, acct_list):
   state = 0
   try:
      f = open(file_, 'r')
      csv_obj = csv.reader(f)
   except:
      print '***** error: File '+file_+' not found. *****'
      state = 1
   if state == 0:
      for row in csv_obj:
         try:
            acct_list.append(row[10])
         except:
            pass
      f.close()
      acct_list.pop(0)
   else:
      pass

def create_report(file_, acct_list):
   state = 0
   report = open('report.txt', 'a')
   try:
      f = open(file_, 'r')
      csv_obj = csv.reader(f)
   except:
      print '***** error: File '+file_+' not found. *****'
      state = 1
   if state == 0:   
      dic = {}

      for row in csv_obj:
         try:
            acct = row[7]
            name = row[3]
            dic[acct] = name
         except:
            print 'end of 2nd csv file'
      for i in accts:
         try:
            info = dic[i]+'\t\t'+i+'\n'
            report.write(info)
         except:
            pass
         report.close()
         f.close()
      else:
         pass

for item in rpt_list:
   create_acct_keys(item, accts) 
for item in fcr_list:
   create_report(item, accts)  


