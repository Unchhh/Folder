# -*- coding: utf-8 -*-
'''
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''


trunk_mode_template = [
    'switchport mode trunk', 'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'
]

trunk_config = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}

#Решение
def generate_trunk_config (intf_vlan_mapping, trunk_template):
	ans1={}
	for inter,vlan in intf_vlan_mapping.items():
		ans=[]
		for i in range(0,len(trunk_template),1):
			if i==2:
				for j in range(0,len(vlan)):
					vlan[j]=str(vlan[j])
				ans.append('{} {}'.format(trunk_template[i],','.join(vlan)))
				continue
			ans.append(trunk_template[i])
		ans1[inter]=ans
	return ans1

print (generate_trunk_config(trunk_config,trunk_mode_template))
