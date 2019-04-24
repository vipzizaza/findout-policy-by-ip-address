# _*_ coding : utf-8 _*_

import os
import re
import pandas

pandas.set_option('display.max_colwidth', 280)
pandas.set_option('display.max_columns', 100)
pandas.set_option('display.width', 500)
f = pandas.read_csv(r'J10-NFJD-PB-ZYC-FW0001-FG3950B_20190416_1015.conf', names='a')
rows = int(f.count())
print(rows)

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

i = 100
while i <= rows-8:
    per_line_6 = str(f.iloc[i-6]).split()
    per_line_6.pop()
    per_line_6.pop()
    per_line_6.pop()
    per_line_6.pop()
    per_line_6.remove('a')

    per_line_5 = str(f.iloc[i - 5]).split()
    per_line_5.pop()
    per_line_5.pop()
    per_line_5.pop()
    per_line_5.pop()
    per_line_5.remove('a')

    per_line_4 = str(f.iloc[i - 4]).split()
    per_line_4.pop()
    per_line_4.pop()
    per_line_4.pop()
    per_line_4.pop()
    per_line_4.remove('a')

    per_line_3 = str(f.iloc[i - 3]).split()
    per_line_3.pop()
    per_line_3.pop()
    per_line_3.pop()
    per_line_3.pop()
    per_line_3.remove('a')

    per_line_2 = str(f.iloc[i - 2]).split()
    per_line_2.pop()
    per_line_2.pop()
    per_line_2.pop()
    per_line_2.pop()
    per_line_2.remove('a')

    per_line_1 = str(f.iloc[i - 1]).split()
    per_line_1.pop()
    per_line_1.pop()
    per_line_1.pop()
    per_line_1.pop()
    per_line_1.remove('a')

    per_line = str(f.iloc[i]).split()
    per_line.pop()
    per_line.pop()
    per_line.pop()
    per_line.pop()
    per_line.remove('a')

    per_line1 = str(f.iloc[i + 1]).split()
    per_line1.pop()
    per_line1.pop()
    per_line1.pop()
    per_line1.pop()
    per_line1.remove('a')

    per_line2 = str(f.iloc[i + 2]).split()
    per_line2.pop()
    per_line2.pop()
    per_line2.pop()
    per_line2.pop()
    per_line2.remove('a')

    per_line3 = str(f.iloc[i + 3]).split()
    per_line3.pop()
    per_line3.pop()
    per_line3.pop()
    per_line3.pop()
    per_line3.remove('a')

    per_line4 = str(f.iloc[i + 4]).split()
    per_line4.pop()
    per_line4.pop()
    per_line4.pop()
    per_line4.pop()
    per_line4.remove('a')

    per_line5 = str(f.iloc[i + 5]).split()
    per_line5.pop()
    per_line5.pop()
    per_line5.pop()
    per_line5.pop()
    per_line5.remove('a')

    per_line6 = str(f.iloc[i + 6]).split()
    per_line6.pop()
    per_line6.pop()
    per_line6.pop()
    per_line6.pop()
    per_line6.remove('a')

    per_line7 = str(f.iloc[i + 7]).split()
    per_line7.pop()
    per_line7.pop()
    per_line7.pop()
    per_line7.pop()
    per_line7.remove('a')

    # print per_line
    for ipaddr in ip_list:
        for word in per_line:
            regex = re.compile('.*' + ipaddr + r'\D.*')
            if regex.search(word):
                print('---------------------------------------------------')
                print(per_line_6)
                print(per_line_5)
                print(per_line_4)
                print(per_line_3)
                print(per_line_2)
                print(per_line_1)
                print(per_line)
                print(per_line1)
                print(per_line2)
                print(per_line3)
                print(per_line4)
                print(per_line5)
                if re.findall('.*next.*', word):
                    print(per_line6)
                    continue
                if re.findall('next', word):
                    print(per_line7)
                    continue
    i += 1
