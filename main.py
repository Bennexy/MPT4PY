import sys
sys.path.append(".")
from multiprocessing import cpu_count

ips = [line.rstrip() for line in open('hosts')]

for host in ips:
    print(host)

string = ""

for i in range(0, 1200):
    string += "t"

test = str.encode(string, 'utf-8')

print(test.__sizeof__(), str.encode(str(cpu_count()), 'utf-8'))



string = "doies test"


