# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
#Решение
answer=input("Enter network/mask: ")
network =answer[0:answer.find('/')].split('.') 
mask = answer[answer.find('/')+1:]
binmask= '1'*int(mask) + '0'*(32-int(mask))
print ('Network:\n{:12}{:12}{:12}{:12}\n{:08b}    {:08b}    {:08b}    {:08b}    \n\nMask:\n/{}\n{:<12}{:<12}{:<12}{:<12}\n{:12}{:12}{:12}{:12}'.
format(network[0],network[1],network[2],network[3],int(network[0]),int(network[1]),int(network[2]),int(network[3]),mask,
int(binmask[0:8],2),int(binmask[8:16],2),int(binmask[16:24],2),int(binmask[24:32],2),binmask[0:8],binmask[8:16],binmask[16:24],binmask[24:32]))
