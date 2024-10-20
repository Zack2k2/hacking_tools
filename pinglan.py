import socket
from datetime import datetime
import subprocess
# Author @inforkgodara

ip_address = input("IP Address: ")
splitted_ip_digits = ip_address.split('.')
dot = '.'

first_three_ip_digits = splitted_ip_digits[0] + dot + splitted_ip_digits[1] + dot + splitted_ip_digits[2] + dot
starting_number = int(input("Starting IP Number: "))
ending_number = int(input("Ending IP Number: "))
ending_number = ending_number + 1
start_time = datetime.now()

def scan(ip_address):
    result = subprocess.call(['ping','-c','3',ip_address])
    if result == 0:
        return 1
    else:
        return 0

def execute():
    for ip in range(starting_number, ending_number):
        ip_address = first_three_ip_digits + str(ip)
        print("testing ", ip_address)
        if (scan(ip_address)):
            print("\t",ip_address, " is live")

execute()
end_time = datetime.now()
total_time = end_time - start_time

print("Scanning completed in: ", total_time)
