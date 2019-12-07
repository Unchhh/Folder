# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
#Решение
b=1
while b:
	ip = input ('Введите IP-адрес: ')
	ip_bytes = ip.split('.')
	if len(ip_bytes)==4:
		for octet in ip_bytes:
			if octet.isdigit() and int(octet)>=0 and  int(octet)<=255:
				pass
			else:
				print('Неправильный IP-адрес')
				break
		else:
			if int(ip_bytes[0])>=1 and int(ip_bytes[0])<=223:
				print('unicast')
			elif int(ip_bytes[0])>=224 and int(ip_bytes[0])<=239:
				print('multicast')
			elif ip=='255.255.255.255':
				print('local broadcast')
			elif ip=='0.0.0.0':
				print('unassigned')
			else:
				print('unused')
			b=0
	else:
		print('Неправильный IP-адрес')
