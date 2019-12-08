# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN

В результате должен получиться такой вывод:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
#Решение
i=0
st = []
st1=[]
with open ('CAM_table.txt') as f:
	for s in f:
		i+=1
		if i>6:
			st.append(s.strip().split())
for i in range (0,len(st)):
	for j in range(i+1,len(st)):
		if int(st[i][0])>int(st[j][0]):
			st1=st[i]
			st[i]=st[j]
			st[j]=st1
	print(' {:<7}{:<17}{}'.format(st[i][0],st[i][1],st[i][3]))

