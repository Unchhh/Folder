# -*- coding: utf-8 -*-
'''
Задание 17.2b

Создать функцию transform_topology, которая преобразует топологию в формат подходящий для функции draw_topology.

Функция ожидает как аргумент имя файла в формате YAML, в котором хранится топология.

Функция должна считать данные из YAML файла, преобразовать их соответственно, чтобы функция возвращала словарь такого вида:
    {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
     ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}

Функция transform_topology должна не только менять формат представления топологии, но и удалять дублирующиеся соединения (их лучше всего видно на схеме, которую генерирует draw_topology).

Проверить работу функции на файле topology.yaml. На основании полученного словаря надо сгенерировать изображение топологии с помощью функции draw_topology.
Не копировать код функции draw_topology.

Результат должен выглядеть так же, как схема в файле task_17_2b_topology.svg

При этом:
* Интерфейсы должны быть записаны с пробелом Fa 0/0
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме
* На схеме не должно быть дублирующихся линков


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''
#Решение

import re
import yaml
from task_17_2a import generate_topology_from_cdp as gen
from draw_network_graph import draw_topology as dr

def transform_topology (file_name):
	ans={}
	with open (file_name) as f:
		d = yaml.safe_load(f)
	for loc_name, value in d.items():
		for loc_inter, value1 in value.items():
			a =tuple(value1.items())[0]
			if a not in list(ans.keys()):
				ans[(loc_name,loc_inter)]=a
	dr(ans,'test')
	return ans


#print(transform_topology('topology.yaml' ))
#print(gen(['sh_cdp_n_sw1.txt','sh_cdp_n_r1.txt','sh_cdp_n_r2.txt','sh_cdp_n_r3.txt','sh_cdp_n_r4.txt','sh_cdp_n_r5.txt','sh_cdp_n_r6.txt'],'topology.yaml' ))
