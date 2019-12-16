# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
#Решение
def get_int_vlan_map (config_filename='config_sw2.txt'):
	temp=[]
	with open(config_filename) as f:
		for line in f:
			if line.startswith('interface') or line.startswith(' switchport access vlan') or line.startswith(' switchport trunk allowed') or line.startswith(' switchport mode acc'):
				temp.append(line.rstrip())
	access={}
	trunk={}
	for i in range(0,len(temp)):
		if temp[i].startswith('interface') and i<len(temp)-1:
			if temp[i+1].startswith(' ') and i<len(temp)-1 and temp[i+2].startswith(' '):
				access[temp[i].split()[1]]=int(temp[i+2].split()[3]);
			elif temp[i+1].startswith(' switchport mode acc'):
				access[temp[i].split()[1]]=1;
			elif temp[i+1].startswith(' switchport trunk all'):
				temp1 =temp[i+1].split()[4].split(',')
				for j in range(0,len(temp1)):
					temp1[j]=int(temp1[j])
				trunk[temp[i].split()[1]]=temp1;
	tuple1=(access,trunk)
	return tuple1
