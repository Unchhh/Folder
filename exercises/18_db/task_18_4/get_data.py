from sys import argv
from tabulate import tabulate as ta
import sqlite3 as sq

def check_arg ():
	par=['mac', 'ip', 'vlan', 'interface', 'switch']
	if len(argv)==1:
		searcher()
	elif len (argv)==3 and argv[1] in par:
		searcher(argv[1],argv[2])
	elif len (argv)==3 and argv[1] not in par:
		print('Данный параметр не поддерживается.\nДопустимые значения параметров: {}'.format(','.join(par)))
	else:
		print('Пожалуйста, введите два или ноль аргументов')

def searcher (name='a',value='a'):
	con=sq.connect('dhcp_snooping.db')
	d ={'a':'select * from dhcp','b':'select * from dhcp where {}=\'{}\''.format(name,value)}
	ans,ans1=[],[]
	with con:
		if name=='a':
			print('В таблице dhcp такие записи:\n')
			c=d['a']
		else:
			print('Информация об устройствах с такими параметрами: {} {}\n'.format(name,value))
			c=d['b']
	for tup in con.execute(c):
		if int(tup[5])==1:
			ans.append(tup)
		else:
			ans1.append(tup)
	if ans!=[]:
		print('Активные записи:\n{}\n'.format(ta(ans)))
	if ans1!=[]:
		print('Неактивные записи:\n{}'.format(ta(ans1)))
	if ans==[] and ans1 ==[]:
		print('Информация отсуствует.')
		
if __name__=='__main__':
	check_arg()
