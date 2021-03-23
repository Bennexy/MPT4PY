import sys
sys.path.append()
from multiprocessing import Pool

ips = [line.rstrip() for line in open('hosts')]

for ip in ips:
    print(ip)