import re
import sqlite3 as sq
import os
import yaml as ya
from datetime import datetime as da,timedelta as ti
from tabulate import tabulate as ta

def create_db (name,scheme):
	if os.path.exists(name):
		print('База данных существует')
	elif not os.path.exists(name):
		print('Невозможно создать БД, файл со схемой {} отсуствует'.format(scheme))
	else:
		con= sq.connect(name)
		with open (scheme) as f:
			con.executescript(f.read())
			print ('Создаю базу данных...')

def get_all_data (file_name):
	if not os.path.exists(file_name):
		print('Файл БД {} отсуствует'.format(file_name))
	else:
		con=sq.connect(file_name)
		ans,ans1=[],[]
		for tup in con.execute('select * from dhcp'):
			if int(tup[5])==1:
				ans.append(tup)
			else:
				ans1.append(tup)
		tab(ans,ans1)
		
def get_data (file_name, key ,val):
	if not os.path.exists(file_name):
		print('Файл БД {} отсуствует'.format(file_name))
	else:
		con=sq.connect(file_name)
		ans,ans1=[],[]
		for tup in con.execute('select * from dhcp where {}=\'{}\''.format(key,val)):
			if int(tup[5])==1:
				ans.append(tup)
			else:
				ans1.append(tup)
		tab(ans,ans1)

def add_data_switches(db_file,file_name):
	for ff in file_name:
		if not all ([os.path.exists(ff), os.path.exists(db_file)]):
			print('Необходимые файл БД {} и файл с данными о коммутаторах {} отсуствуют'.format(db_file,ff))
		else:
			ans=[]
			with open (ff) as f:
				for k,v in ya.safe_load(f)['switches'].items():
					ans.append((k,v))
			db_add_data('switches', ans,db_file)

def add_data(db_file,file_name):
	sw_names,ans=set(),[]
	reg=re.compile(r'(\w+)_dhcp_snooping.txt')
	reg1 = re.compile(r'(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
	for ff in file_name:
		if not all ([os.path.exists(ff), os.path.exists(db_file)]):
			print('Необходимые файл БД {} и файл с данными dhcp {} отсуствуют'.format(db_file,ff))
		else:
			with open (ff) as f:
				for line in f:
					match = reg1.search(line)
					if match:
						ans.append(tuple(list(match.groups())+ [reg.search(ff).group(1)]))
						sw_names.add(reg.search(ff).group(1))
	db_add_data ('dhcp',ans,db_file,sw_names)
							
		
def db_add_data (table_name, data_list, db_file, sw_list=set()):
	command ={'switches':'replace into switches (hostname, location) values (?, ?)','dhcp':'replace into dhcp values (?, ?, ?, ?, ?, ?, ?)'}
	con = sq.connect(db_file)
	with con:
		if sw_list!=set():
			for sw in sw_list:
				con.execute('update {} set active = 0 where switch = \'{}\''.format(table_name,sw))
			week_ago = da.today().replace(microsecond=0)- ti(days=7)
			for l in con.execute('select * from dhcp where active=0'):
				mac = l[0]
				if da.strptime(l[6],'%Y-%m-%d %H:%M:%S') <week_ago:
					con.execute('delete from dhcp where mac=\'{}\''.format(mac))			
		for r in data_list:
			try:
				if table_name=='dhcp':
					con.execute(command[table_name], tuple(list(r)+[1,'{0:%Y}-{0:%m}-{0:%d} {0:%H}:{0:%M}:{0:%S}'.format(da.now())]))
				else:	
					con.execute(command[table_name], r)
			except sq.IntegrityError as e:
				print('При добавлении данных: {} Возникла ошибка: {}'.format(r,e))

def tab (ans,ans1):
	if ans!=[]:
		print('Активные записи:\n{}\n'.format(ta(ans)))
	if ans1!=[]:
		print('Неактивные записи:\n{}'.format(ta(ans1)))
	if ans==[] and ans1 ==[]:
		print('Информация отсуствует.')

