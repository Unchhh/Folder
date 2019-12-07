# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
#Решение
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
else:
	print('Неправильный IP-адрес')
