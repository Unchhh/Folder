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
	ans=[]
	with con:
		if name=='a':
			for tup in con.execute('select * from dhcp'):
				ans.append(tup)
			print('В таблице dhcp такие записи:\n{}'.format(ta(ans)))
		else:
			for tup in con.execute('select * from dhcp where {}=\'{}\''.format(name,value)):
				ans.append(tup)
			print('Информация об устройствах с такими параметрами: {} {}\n{}'.format(name,value,ta(ans)))
			if ans==[]:
				print('Отсуствует.')
		
if __name__=='__main__':
	check_arg()
