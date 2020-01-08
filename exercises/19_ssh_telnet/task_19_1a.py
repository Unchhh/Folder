# -*- coding: utf-8 -*-
'''
Задание 19.1a

Скопировать функцию send_show_command из задания 19.1 и переделать ее таким образом,
чтобы обрабатывалось исключение, которое генерируется
при ошибке аутентификации на устройстве.

При возникновении ошибки, на стандартный поток вывода должно выводиться сообщение исключения.

Для проверки измените пароль на устройстве или в файле devices.yaml.
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
	except netmiko.ssh_exception.NetMikoAuthenticationException as e:
		print('Error: {}'.format(e))
		return'\n'
	else:	
		return res
	
if __name__=='__main__':
	with open('devices.yaml') as f:
		param=ya.safe_load(f)
		for  dev in param:
			print(send_show_command(dev,'show ip int bri'))
