#!/usr/bin/python

import csv, os,  time


rpt_list = []
fcr_list = []
root, folders, files = os.walk('.').next()
for item in files:
    if item.startswith('FCRALLDetailReport'):
        fcr_list.append(item)
    elif item.startswith('RptCareTCDetail'):
        rpt_list.append(item)




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

def write_header(target_file, report_file):
    info = report_file+'\n'
    headers = ['ACCOUNT NUMBER','AGENT NAME','UCID']
    f = open(target_file,'a')
    for i in headers:
        info += i+'\t\t\t'
    info +='\n\n'
    f.write(info)
    f.close()

def print_stuff(list_):
    c = 0
    for i in list_:
        c += 1
	print i+': '+str(c)

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
        list_ = []
	info =''
	
    for row in csv_obj:
        acct = row[7]
        if len(acct) != 16:
	    acct = acct[0:-1]
        if acct in acct_list:
	    list_.append(acct)
	    name = row[3]
	    name = name[0:-1]
	    list_.append(name)
	    UCID = row[26]
	    if len(UCID) != 20:
	        UCID = UCID[0:-1]
	    list_.append(UCID)
	   
    for i in list_:
        info += i+'\t\t'
    info+='\n\n'
    report.write(info)
    f.close()
    print_stuff(list_)
    report.close()
    

for item in rpt_list:
    create_acct_keys(item, accts) 

for item in fcr_list:
    write_header('report.txt', item)
    create_report(item, accts)



