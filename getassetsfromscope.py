#!/usr/bin/python3
import sys
import csv

def main():
    wildcard_filename = 'wildcards.txt'
    domains_filenmae = 'domains.txt'
    csvfile = 'scopes.csv'
    
    domains = []
    wildcards = []
    if len(sys.argv) < 2:
        print("{0} <scopes.csv>".format(sys.argv[0]))
        sys.exit(1)
    
    csvfd = open(sys.argv[1])
    csvreader = csv.reader(csvfd)

    
    for row in csvreader:
        if row[1] == 'URL':
            domains.append(row[0]+'\n')
        if row[1] == 'WILDCARD':
            wildcards.append(row[0]+'\n')

    
    wildcardsfd = open(wildcard_filename,'w+')
    domainsfd = open(domains_filenmae,'w+')

    wildcardsfd.writelines(wildcards)
    domainsfd.writelines(domains)

    wildcardsfd.close()
    domainsfd.close()



if __name__ == '__main__':
    main()








