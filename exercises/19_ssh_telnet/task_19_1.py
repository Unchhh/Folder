# -*- coding: utf-8 -*-
'''
Задание 19.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к одному устройству и выполняет указанную команду.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* command - команда, которую надо выполнить

Функция возвращает строку с выводом команды.

Скрипт должен отправлять команду command на все устройства из файла devices.yaml с помощью функции send_show_command.

'''

command = 'sh ip int br'

#Решение
import yaml as ya
from netmiko import ConnectHandler as co

def send_show_command (device, command):
	print ('Подключение к устройству {}\n'.format(device['ip']))
	with co(**device) as ssh:
		ssh.enable()
		res=ssh.send_command(command)
	return res
	
if __name__=='__main__':
	with open('devices.yaml') as f:
		param=ya.safe_load(f)
		for  dev in param:
			print(send_show_command(dev,command))
