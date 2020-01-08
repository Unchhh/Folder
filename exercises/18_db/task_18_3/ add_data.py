import re
import sqlite3 as sq
import os
import yaml as ya

def table_data(file_list):
	sw_names,ans,ans1=set(),[],[]
	reg=re.compile(r'(\w+)_dhcp_snooping.txt')
	reg1 = re.compile(r'(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')

	for files in file_list:
		with open(files) as f:
			for line in f:
				match = reg1.search(line)
				if match:
					ans.append(tuple(list(match.groups())+ [reg.search(files).group(1)]))
					sw_names.add(reg.search(files).group(1))
	with open ('switches.yml') as f:
		for k,v in ya.safe_load(f)['switches'].items():
			ans1.append((k,v))
	if not os.path.exists('dhcp_snooping.db'):
		print('База данных не существует. Перед добавлением данных, ее надо создать')
	else:
		db_add_data ('switches',ans1)
		db_add_data ('dhcp',ans,sw_names)
		


def db_add_data (table_name, data_list, sw_list=set()):
	command ={'switches':'insert into switches (hostname, location) values (?, ?)','dhcp':'replace into dhcp values (?, ?, ?, ?, ?, ?)'}
	con = sq.connect('dhcp_snooping.db')
	print('Добавляю данные в таблицу {}...'.format(table_name))
	with con:
		if sw_list!=set():
					for sw in sw_list:
						con.execute('update {} set active = 0 where switch = \'{}\''.format(table_name,sw))
		for r in data_list:
			try:
				if table_name=='dhcp':
					con.execute(command[table_name], tuple(list(r)+[1]))
				else:	
					con.execute(command[table_name], r)
			except sq.IntegrityError as e:
				print('При добавлении данных: {} Возникла ошибка: {}'.format(r,e))
				
if __name__=='__main__':
	table_data(['new_data/sw1_dhcp_snooping.txt','new_data/sw2_dhcp_snooping.txt','new_data/sw3_dhcp_snooping.txt'])
