# -*- coding: utf-8 -*-
'''
Задание 12.3


Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые переданы ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.


Для этого задания нет тестов
'''
from tabulate import tabulate as tab
def print_ip_table (avail,na_avail):
	t ={'Reachable':avail,'Unreachable':na_avail}
	print(tab(t,headers='keys'))

print_ip_table(['10.1.1.1','10.1.1.2'],['10.1.1.7','10.1.1.8','10.1.1.9'])
	