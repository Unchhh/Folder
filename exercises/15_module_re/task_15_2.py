# -*- coding: utf-8 -*-
'''
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

'''
#Решение
import re
def parse_sh_ip_int_br (file_name):
	ans=[]
	r = re.compile(r'(?P<int>\S+) +(?P<ip>((\d+\.){3}\d)|unassigned)( +\S+){2} +(?P<sta>up|down|administratively down) +(?P<pro>up|down)')
	with open(file_name) as f:
		for line in f:
			match=r.search(line)
			if match:
				ans.append((match.group('int'),match.group('ip'),match.group('sta'),match.group('pro')))
	return ans
if __name__=='__main__':
	print(parse_sh_ip_int_br('sh_ip_int_br.txt'))
			
		
