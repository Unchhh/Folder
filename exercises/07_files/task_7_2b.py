# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

#Решение
file_name = ''
try:
	from sys import argv
	file_name = argv[1]
	with open (file_name) as f, open ('config_sw1_cleared.txt', 'w') as f1:
		for s in f:
				for ign in ignore:
					if s.find(ign)!=-1:
						break;
				else:
					f1.write(s)
except (IndexError):
	print('Не введено имя файла!')
except (FileNotFoundError):
	print('Не найдено файла {}!'.format(file_name))
