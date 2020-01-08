# -*- coding: utf-8 -*-
'''
Задание 19.2a

Скопировать функцию send_config_commands из задания 19.2 и добавить параметр verbose,
который контролирует будет ли выводится на стандартный поток вывода
информация о том к какому устройству выполняется подключение.

verbose - это параметр функции send_config_commands, не параметр ConnectHandler!

По умолчанию, результат должен выводиться.

Пример работы функции:

In [13]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...

In [14]: result = send_config_commands(r1, commands, verbose=False)

In [15]:

Скрипт должен отправлять список команд commands на все устройства из файла devices.yaml с помощью функции send_config_commands.
'''
commands = ['logging 10.255.255.1', 'logging buffered 20010', 'no logging console']

#Решение
import yaml as ya
from netmiko import ConnectHandler as co

def send_config_commands (device, config_commands, verbose=True):
	if verbose:
		print ('Подключаюсь к {}...\n'.format(device['ip']))
	with co(**device) as ssh:
		ssh.enable()
		res=ssh.send_config_set(config_commands)
	return res
	
if __name__=='__main__':
	with open('devices.yaml') as f:
		param=ya.safe_load(f)
		for  dev in param:
			print(send_config_commands(dev,commands,0))
