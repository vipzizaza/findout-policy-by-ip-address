# -*- coding:utf-8 -*-

import re

f = open(r'10.2.224.36-20190430-1556.log')
lines = f.readlines()

ip_list = [
'10.2.126.10',
'10.2.126.11',
'10.2.126.51',
'10.2.126.52',
'10.2.126.53',
'10.2.126.54',
'10.2.126.55',
'10.2.126.56',
'10.2.126.57',
'10.2.126.58',
'10.2.126.59',
'10.2.126.7',
'10.2.126.8',
'10.2.126.9',
'10.2.126.0',
'acl advanced name']

i = 1
for line in lines:
    line = line.strip()
    for per_ip_addr in ip_list:
        rex = re.compile('.*' + per_ip_addr + '.*')
        if rex.findall(line):
            print(i, line)
    i += 1
f.close()
