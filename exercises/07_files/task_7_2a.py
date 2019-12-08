# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

#Решение
file_name = ''
try:
	from sys import argv
	file_name = argv[1]
	with open (file_name) as f:
		for s in f:
			if s.startswith('!'):
				continue
			else:
				for ign in ignore:
					if s.find(ign)!=-1:
						break;
				else:
					print(s.rstrip())
except (IndexError):
	print('Не введено имя файла!')
except (FileNotFoundError):
	print('Не найдено файла {}!'.format(file_name))
