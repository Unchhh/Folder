# -*- coding: utf-8 -*-
'''
Задание 17.1

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Для выполнения задания нужно создать две функции.

Функция parse_sh_version:
* ожидает как аргумент вывод команды sh version одной строкой (не имя файла)
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"

У функции write_inventory_to_csv должно быть два параметра:
 * data_filenames - ожидает как аргумент список имен файлов с выводом sh version
 * csv_filename - ожидает как аргумент имя файла (например, routers_inventory.csv), в который будет записана информация в формате CSV
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает


Функция write_inventory_to_csv должна делать следующее:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в CSV файл

В файле routers_inventory.csv должны быть такие столбцы:
* hostname, ios, image, uptime

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается на sh_vers.
Вы можете раскомментировать строку print(sh_version_files), чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.
'''

import glob

sh_version_files = glob.glob('sh_vers*')
#print(sh_version_files)

headers = ['hostname', 'ios', 'image', 'uptime']

#Решение
import re, csv

def parse_sh_version (inp):
	match = re.search(r'.+Version (?P<ver>\S+?),[\s\S]+uptime is (?P<up>.+)\n[\s\S]+ file is "(?P<ima>\S+)"', inp)
	return (match.group('ver'),match.group('ima'),match.group('up'))

def write_inventory_to_csv (file_names, csv_name):
	ans=[headers]
	for files in file_names:
		with open(files) as f:
			ans.append([re.search(r'sh_version_(.+)\.txt',files).group(1)]+list(parse_sh_version(f.read())) )
	with open(csv_name,'w') as w:
		writer=csv.writer(w, quoting= csv.QUOTE_NONNUMERIC)
		for row in ans:
			writer.writerow(row) 
