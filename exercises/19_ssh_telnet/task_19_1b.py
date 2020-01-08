# -*- coding: utf-8 -*-
'''
Задание 19.1b

Скопировать функцию send_show_command из задания 19.1a и переделать ее таким образом,
чтобы обрабатывалось не только исключение, которое генерируется
при ошибке аутентификации на устройстве, но и исключение,
которое генерируется, когда IP-адрес устройства недоступен.

При возникновении ошибки, на стандартный поток вывода должно выводиться сообщение исключения.

Для проверки измените IP-адрес на устройстве или в файле devices.yaml.
'''


#Решение
import yaml as ya
import netmiko
from netmiko import ConnectHandler as co

def send_show_command (device, command):
	try:
		print ('Подключение к устройству {}\n'.format(device['ip']))
		with co(**device) as ssh:
			ssh.enable()
			res=ssh.send_command(command)
	except (netmiko.ssh_exception.NetMikoAuthenticationException,netmiko.ssh_exception.NetMikoTimeoutException) as e:
		print('Error: {}'.format(e))
		return'\n'
	else:	
		return res
	
if __name__=='__main__':
	with open('devices.yaml') as f:
		param=ya.safe_load(f)
		for  dev in param:
			print(send_show_command(dev,'show ip int bri'))
