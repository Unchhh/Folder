# -*- coding: utf-8 -*-
'''
Задание 9.4

Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный файл коммутатора и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (пробелы в начале строки надо удалить).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с '!',
а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command.


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']


def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    '''
    return any(word in command for word in ignore)

#Решение
def convert_config_to_dict (config_filename='config_sw1.txt'):
	temp=[]
	with open(config_filename) as f:
		for line in f:
			if line.startswith('!') or ignore_command(line,ignore):
				continue
			temp.append(line.rstrip())
	temp.pop(0)
	ans={};j=0;ans1=[]
	for i in range(0,len(temp)):
		if not temp[i].startswith(' '):
			j=i ;ans1=[]
			while i+1<len(temp) and temp[i+1].startswith(' '):
				ans1.append(temp[i+1].lstrip())
				i+=1
			ans[temp[j]]=ans1
	return ans

for gl,sub in convert_config_to_dict().items():
	print(sub)

