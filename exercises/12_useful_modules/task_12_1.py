# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
#Решение
import subprocess as sub
import ipaddress as ipd
def ping_ip_addresses (ip_list):
	av,not_av =[],[]
	for ip in ip_list:
		try:
			ipv4 = ipd.ip_address(ip)
		except ValueError:
			not_av.append(ip)
			continue
		result=sub.run(['ping','-c','2','-i','0.2','-w','1','-n', ip], stdout=sub.DEVNULL)
		if result.returncode!=0:
			not_av.append(ip)
		else:
			av.append(ip)
	return (av,not_av)	
	
