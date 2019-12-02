# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
#Решение
from sys import argv
answer=argv[1]
network =answer[0:answer.find('/')].split('.') 
mask = answer[answer.find('/')+1:]
binnetwork= '{:08b}{:08b}{:08b}{:08b}'.format(int(network[0]),int(network[1]),int(network[2]),int(network[3]))[:int(mask)]+'0'*(32-int(mask))
binmask= '1'*int(mask) + '0'*(32-int(mask))
print ('Network:\n{:<12}{:<12}{:<12}{:<12}\n{}    {}    {}    {}    \n\nMask:\n/{}\n{:<12}{:<12}{:<12}{:<12}\n{:12}{:12}{:12}{:12}'.
format(int(binnetwork[:8],2),int(binnetwork[8:16],2),int(binnetwork[16:24],2),int(binnetwork[24:32],2),binnetwork[:8],binnetwork[8:16],binnetwork[16:24],binnetwork[24:32],mask,
int(binmask[0:8],2),int(binmask[8:16],2),int(binmask[16:24],2),int(binmask[24:32],2),binmask[0:8],binmask[8:16],binmask[16:24],binmask[24:32]))
