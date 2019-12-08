# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
#Решение
ospf_routes = []
with open('ospf.txt') as f:
	for line in f:
		ospf_routes.append(line.replace(',','').split())
for routes in ospf_routes:
	routes[0]='OSPF'
	print('{:<24}{}\n{:<24}{}\n{:<24}{}\n{:<24}{}\n{:<24}{}\n{:<24}{}\n'.format('Protocol:',routes[0]
	,'Prefix:',routes[1],'AD/Metric:',routes[2],'Next-Hop:',routes[4],'Last update:',routes[5],'Outbond Interface:',routes[6]))

