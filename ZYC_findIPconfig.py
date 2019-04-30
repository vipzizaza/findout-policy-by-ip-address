# -*- coding:utf-8 -*-

import pandas
import re

pandas.set_option('display.max_colwidth', 280)
pandas.set_option('display.max_columns', 100)
pandas.set_option('display.width', 500)
f = pandas.read_csv(r'NFJD-YHZYC-FW04-HW-8000E.cfg', names='a')
rows = int(f.count())
print(rows)

ip_list = [
'10.102.10.4',
'10.102.10.5',
'10.102.10.6',
'10.102.10.0',
'10.150.0.14',
'10.150.0.15',
'10.150.0.4',
'10.150.0.5',
'10.150.0.0',
'10.151.0.10',
'10.151.0.4',
'10.151.0.5',
'10.151.0.6',
'10.151.0.7',
'10.151.0.8',
'10.151.0.9',
'10.151.0.0',
'10.152.0.132',
'10.152.0.133',
'10.152.0.134',
'10.152.0.135',
'10.152.0.136',
'10.152.0.137',
'10.152.0.138',
'10.152.0.139',
'10.152.0.0',
'10.153.176.4',
'10.153.176.5',
'10.153.176.6',
'10.153.176.0',
'10.153.69.10',
'10.153.69.11',
'10.153.69.12',
'10.153.69.13',
'10.153.69.14',
'10.153.69.15',
'10.153.69.16',
'10.153.69.17',
'10.153.69.4',
'10.153.69.5',
'10.153.69.55',
'10.153.69.56',
'10.153.69.57',
'10.153.69.58',
'10.153.69.59',
'10.153.69.60',
'10.153.69.0',
'10.164.5.61',
'10.164.5.62',
'10.164.5.63',
'10.164.5.0',
'10.166.1.100',
'10.166.1.101',
'10.166.1.102',
'10.166.1.103',
'10.166.1.104',
'10.166.1.105',
'10.166.1.106',
'10.166.1.107',
'10.166.1.108',
'10.166.1.109',
'10.166.1.110',
'10.166.1.52',
'10.166.1.53',
'10.166.1.0']


def get_line(row_num):
    per_line = str(f.iloc[row_num]).split()
    per_line.pop()
    per_line.pop()
    per_line.pop()
    per_line.pop()
    per_line.remove('a')
    return per_line


def find_addr_set_name(row_num):
    f_loc = get_line(row_num)
    # print(f_loc)
    for ip_addr in ip_list:
        if (ip_addr in f_loc) and ('address' in f_loc):
            # print(row_num+2, f_loc)
            previous_line = row_num - 1
            while previous_line > 0:
                if 'address-set' in get_line(previous_line):
                    # print(previous_line+2, get_line(previous_line))
                    if get_line(previous_line)[2] in ip_add_name_list:
                        break
                    else:
                        ip_add_name_list.append(get_line(previous_line)[2])
                    break
                previous_line -= 1


def find_acl_name(row_num):
    f_loc = get_line(row_num)
    # print(f_loc)
    for ip_addr in ip_list:
        if (ip_addr in f_loc) and ('rule' in f_loc):
            # print(row_num+2, f_loc)
            previous_line = row_num - 1
            while previous_line > 0:
                if 'number' in get_line(previous_line):
                    # print(get_line(previous_line))
                    # print(f_loc)
                    if get_line(previous_line)[2] in acl_name_list:
                        break
                    else:
                        acl_name_list.append(get_line(previous_line)[2])
                    break
                previous_line -= 1


ip_add_name_list = []
i = 0
while i <= rows-1:
    find_addr_set_name(i)
    i += 1
ip_add_name_list.pop()
print(ip_add_name_list)
ip_list = ip_list + ip_add_name_list

acl_name_list = []
n = 0
while n <= rows-1:
    find_acl_name(n)
    n += 1
print(acl_name_list)

for acl_name in acl_name_list:
    rule_list_name = 'rule_list_%s' % acl_name
    print(rule_list_name)
    a = 1
    while a <= rows-1:
        f_loc = get_line(a)
        if 'acl' in f_loc and 'number' in f_loc and acl_name in f_loc:
            b = 1
            while b <= 300:
                f_loc_rule = get_line(a+b)
                for per_ip_add in ip_list:
                    if 'rule' in f_loc_rule and per_ip_add in f_loc_rule:
                        print(f_loc_rule)
                    elif 'acl' in f_loc and 'number' in f_loc:
                        continue
                    else:
                        print('why can i find the acl number')
                b += 1
        a += 1
