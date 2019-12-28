# -*- coding: utf-8 -*-
'''
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
'''
#Решение
import re
def convert_ios_nat_to_asa (r_f,w_f):
	reg = re.compile(r'ip nat (\w+) source (\w+) (\w+) ((\d+\.){3}\d+) (\d{1,5}) interface (\S+) (\d{1,5})')
	with open(r_f) as r, open(w_f,'w') as  w:
		ans=''
		for line in r:
			match=reg.search(line)
			if(match):
				ans+='object network LOCAL_{0}\n host {0}\n nat (inside,outside) {1} interface service {2} {3} {4}\n'.format(match.group(4),match.group(2),match.group(3),match.group(6),match.group(8))
		print(ans)
		w.write(ans)

convert_ios_nat_to_asa('cisco_nat_config.txt','result.txt')				
		
		

