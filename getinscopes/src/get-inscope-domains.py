import sys
import csv

def main():
    
    #first handle command lines.
    argc = len(sys.argv);

    if (argc < 3 or '--help' in sys.argv):
        print("{0} <csv_file_of_scope> <txt_file_to_savedomains> [-q quite]".format(sys.argv[0]))
        sys.exit(0)
    
    if '--help' in sys.argv:
        print("{0} ",end='');
        print("<csv_file_of_scope> <txt_file_to_savedomains> [-q quite] ");
        print("fetching severity ")
        print(" -c : for critical severity domains");
        print(" -h : for high severity domains")
        print(" -m : for medium severity domains")
        print(" -l : for low severity domains")
        
        sys.exit(0)

    scope_file_name = sys.argv[1];
    domain_txt = sys.argv[2]

    scope_fd = open(scope_file_name)
    scope_csv_reader = csv.reader(scope_fd)
    datalist = list(scope_csv_reader)

    n_datalist = len(datalist)
    domain_list = []            # contains the domain


    include_severity = False;   # to get severity or not.
    
    severity = {"critical":False,"high":False,"medium":False,"low":False}



    if '-c' in sys.argv:
        include_severity = True
        severity['critical'] = True;

    if '-h' in sys.argv:
        include_severity = True;
        severity['high'] = True
    if '-m' in sys.argv:
        include_severity = True;
        severity['medium'] = True

    if '-l' in sys.argv:
        include_severity = True;
        severity['low'] = True

    if include_severity:
        if severity['critical']:
            for row in datalist:
                if row[8] == 'critical':
                    domain_list.append(row[0])
        if severity['high']:
            for row in datalist:
                if row[8] == 'high':
                    domain_list.append(row[0])

    else:
        # loop through every row in the csv excluding the top row.
        for row_number in range(1,n_datalist):          
            domain_list.append(datalist[row_number][0])

    # print data if not specified to keep quite.
    if ('-q' not in sys.argv):
        for row in domain_list:
            print(row)

    
    try:
        with open(domain_txt,'w') as domain_txt_fd:
            for row in domain_list:
                domain_txt_fd.write(row+'\n')

    except IOError:
        print("Program wasn't able to write to a file.")


if __name__ == "__main__":
    main()
