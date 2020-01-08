import re
import sqlite3 as sq
import os
import yaml as ya

def table_data():
	ans,ans1=[],[]
	reg=re.compile(r'(\S+)_dhcp_snooping.txt')
	reg1 = re.compile(r'(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
	dhcp_filelist = [x for x in os.listdir('.') if reg.search(x)]
	for files in dhcp_filelist:
		with open(files) as f:
			for line in f:
				match = reg1.search(line)
				if match:
					ans.append(tuple(list(match.groups())+ [reg.search(files).group(1)]))
	with open ('switches.yml') as f:
		for k,v in ya.safe_load(f)['switches'].items():
			ans1.append((k,v))
	if not os.path.exists('dhcp_snooping.db'):
		print('База данных не существует. Перед добавлением данных, ее надо создать')
	else:
		db_add_data ('switches',ans1)
		db_add_data ('dhcp',ans)
		


def db_add_data (table_name, data_list):
	command ={'switches':'insert into switches (hostname, location) values (?, ?)','dhcp':'insert into dhcp (mac, ip, vlan, interface, switch) values (?, ?, ?, ?, ?)'}
	con = sq.connect('dhcp_snooping.db')
	print('Добавляю данные в таблицу {}...'.format(table_name))
	with con:
		for r in data_list:
			try:
				con.execute(command[table_name], r)
			except sq.IntegrityError as e:
				print('При добавлении данных: {} Возникла ошибка: {}'.format(r,e))
				
if __name__=='__main__':
	table_data()
