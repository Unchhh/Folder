import os
import sqlite3 as sq

def create_db (name):
	if os.path.exists(name):
		print('База данных существует')
	else:
		con= sq.connect(name)
		with open ('dhcp_snooping_schema.sql') as f:
			con.executescript(f.read())
			print ('Создаю базу данных...')
			
if __name__=='__main__':
	create_db('dhcp_snooping.db')
	
