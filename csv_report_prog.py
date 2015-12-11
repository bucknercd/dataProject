import csv, os

def create_acct_keys(file_, acct_list):
    f = open(file_, 'r')
    csv_obj = csv.reader(f)
    for row in csv_obj:
        acct_list.append(row[10])
    f.close()
    acct_list.pop(0)

def write_header(out_file):
    headers = ['ACCOUNT NUMBER','AGENT NAME','ORIGINAL UCID','SUPERVISOR NAME']
    f = open(out_file,'a')
    writer = csv.writer(f,quoting=csv.QUOTE_MINIMAL)
    writer.writerow(headers)
    f.close()

def create_report(file_, acct_list):
    report = open('report.csv', 'ab')
    writer = csv.writer(report,quoting=csv.QUOTE_MINIMAL)
    f = open(file_, 'rb')
    csv_obj = csv.reader(f)
    for row in csv_obj:
        list_ = []
        acct = row[7]
        if len(acct) != 16:
	    acct = acct[0:-1]
        if acct in acct_list:
	    list_.append(acct)
	    name = row[3]
	    name = name[0:-2]
	    list_.append(name)
	    UCID = row[26]
	    if len(UCID) != 20:
	        UCID = UCID[0:-1]
	    if UCID.startswith('0'):
	        UCID = '*'+UCID
	    list_.append(UCID)
	    sup_name = row[1]
	    sup_name = sup_name[0:-2]
	    list_.append(sup_name)
	    print list_
            writer.writerow(list_)
    f.close()
    report.close()

if __name__ == '__main__':
    accts = []
    rpt_list = []
    fcr_list = []
    root, folders, files = os.walk('.').next()
    for item in files:
        if item.startswith('FCRALLDetailReport'):
            fcr_list.append(item)
        elif item.startswith('RptCareTCDetail'):
            rpt_list.append(item)
    for file_ in rpt_list:
        try:
            create_acct_keys(file_, accts)
        except IOError as e:
    	    print '***** error: File '+file_+' not found. *****'
        except IndexError as e:
    	    print e
    write_header('report.csv')
    for file_ in fcr_list:
        try:
            create_report(file_, accts)
        except IOError as e:
    	    print '***** error: File '+file_+' not found. *****'
        except IOError as e:
    	    print e
