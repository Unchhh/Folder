# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
#Решение
def get_int_vlan_map (config_filename='config_sw1.txt'):
	temp=[]
	with open(config_filename) as f:
		for line in f:
			if line.startswith('interface') or line.startswith(' switchport access vlan') or line.startswith(' switchport trunk allowed'):
				temp.append(line.strip())
	access={}
	trunk={}
	for i in range(0,len(temp),2):
		if temp[i].startswith('interface') and i<len(temp)-1 and temp[i+1].startswith('switchport a'):
			access[temp[i].split()[1]]=int(temp[i+1].split()[3])
		elif temp[i].startswith('interface') and i<len(temp)-1 and temp[i+1].startswith('switchport t'):
			temp1 =temp[i+1].split()[4].split(',')
			for j in range(0,len(temp1)):
				temp1[j]=int(temp1[j])
			trunk[temp[i].split()[1]]=temp1
	tuple1=(access,trunk)
	return tuple1
