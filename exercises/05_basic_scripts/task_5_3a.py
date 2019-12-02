# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

#Решение
int_mode= input('Введите режим работы интерфейса (access/trunk): ')
int_type= input('Введите тип и номер интерфейса: ')
dict1 = {'access':'Введите номер VLAN: ','trunk':'Введите разрешенные VLANы: '}
int_vlans= input(dict1[int_mode])
access='\n\ninterface {}\n{}\n'.format(int_type,access_template[0])+access_template[1].format(int_vlans)+ '\n{}\n{}\n{}\n'.format(access_template[2],access_template[3],access_template[4])
trunk='\n\ninterface {}\n{}\n{}\n'.format(int_type,trunk_template[0],trunk_template[1])+trunk_template[2].format(int_vlans)
dict = {'access':access,'trunk':trunk}
print(dict[int_mode])
