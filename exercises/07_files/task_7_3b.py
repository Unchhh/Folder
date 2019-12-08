# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
#Решение
i1=0
j1=1
st = []
st1=[]
while 1:
	vlan_n= input('Введите номер VLAN: ')
	if (vlan_n.isdigit()):
		break
	print('Введённый Vlan некорректен!')
with open ('CAM_table.txt') as f:
	for s in f:
		i1+=1
		if i1>6:
			st.append(s.strip().split())
for i in range (0,len(st)):
	for j in range(i+1,len(st)):
		if int(st[i][0])>int(st[j][0]):
			st1=st[i]
			st[i]=st[j]
			st[j]=st1
	if int(st[i][0])==int(vlan_n):
		print(' {:<7}{:<17}{}'.format(st[i][0],st[i][1],st[i][3]))
		j1=0
	if i==len(st)-1 and j1==1:
		print('Vlan {} в файле CAM_table.txt не обнаружен!'.format(vlan_n))
