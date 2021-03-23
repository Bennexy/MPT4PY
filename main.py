import sys
sys.path.append(".")
from multiprocessing import cpu_count

ips = [line.rstrip() for line in open('hosts')]

for host in ips:
    print(host)

print(str.encode('test', 'utf-8'), str.encode(str(cpu_count())))