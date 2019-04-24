#coding=utf-8

import pandas
import re

pandas.set_option('display.max_colwidth', 280)
pandas.set_option('display.max_columns', 100)
pandas.set_option('display.width', 500)
f = pandas.read_csv('J11-NFJD-PB-ZYC-FW0001-FG3950B_20190409_0952.conf', names='a', nrows=3000)
ip_list = ['10.1.118.11',
'10.1.118.12',
'10.1.118.0',
'10.1.140.1',
'10.1.140.12',
'10.1.140.13',
'10.1.140.2',
'10.1.140.3',
'10.1.140.4',
'10.1.140.0',
'10.1.24.1',
'10.1.24.2',
'10.1.24.3',
'10.1.24.5',
'10.1.24.0',
'10.1.89.1',
'10.1.89.2',
'10.1.89.3',
'10.1.89.4',
'10.1.89.0'
]

rows = int(f.count())
print rows
i = 0
while i <= rows-1:
    line = str(f.iloc[i])
    line = line.split()
    if '10.1.24.3' in line:
        print line
    i += 1
