import sys
sys.path.append(".")
from multiprocessing import cpu_count

ips = [line.rstrip() for line in open('hosts')]

for host in ips:
    print(host)

test = str.encode(host, 'utf-8')

print(test.__sizeof__(), str.encode(str(cpu_count()), 'utf-8'))



string = "doies test"

print(list(string))

