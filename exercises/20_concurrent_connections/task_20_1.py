# -*- coding: utf-8 -*-
'''Задание 20.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.
'''
#Решение
import logging
import subprocess as sub
import ipaddress as ipa
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime as da

def ping (ip):
	try:
		ipv4 = ipa.ip_address(ip)
		result=sub.run(['ping','-c','2','-i','0.2','-w','1','-n', ip], stdout=sub.DEVNULL)
		return [ip,result.returncode]
	except ValueError: 
		return [ip,1]		

def ping_ip_addresses (ip_list,limit=3):
	sta=da.now()
	logging.basicConfig(format='%(threadName)s %(name)s %(levelname)s %(message)s',level=logging.INFO)
	with ThreadPoolExecutor (max_workers=limit) as execut:
		avail,no_avail =[],[]
		result=execut.map(ping,ip_list)
	for res in result:
		if res[1]==0:
			print('Ip {} доступен'.format(res[0]))
			avail.append(res[0])
		else:
			no_avail.append(res[0])
			print('Ip {} не доступен'.format(res[0]))
	print('Время выполнения скрипта: {}'.format(da.now()-sta))
	return (avail,no_avail)

if __name__=='__main__':
	print (ping_ip_addresses(['192.168.100.1','45.56.58.85','127.0.0.1','78.125.45.77','192.168.100.2','12.28'],6))			
