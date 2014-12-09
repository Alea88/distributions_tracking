# --------------------------------------------------------------------------------------------------------------
# UTILITY TO RETRIEVE THE TURN BY TURN DATA FROM AN SQLite DB
# GIOVANNA CAMPOGIANI
# LAST MODFIIED: 25/09/2014
# --------------------------------------------------------------------------------------------------------------

import sqlite3
import numpy as np

def row_read(command,cur):
	
	lst=list()
	i=1
	for row in cur.execute('%s' %command):
		#i=i+1
		#if i==100:
			lst+=list(row)
		#	i=1
	return lst
	
	
	
	
	
def row_read_all(command,cur):
	
	lst=list()
	for row in cur.execute('%s' %command):
			lst+=list(row)
	return lst
	
	
	
	
def read_from_db(col_name,dbname,tablename,cond_name,cond_value):

	command='SELECT '+col_name+' FROM '+tablename+' WHERE '+cond_name+'='+str(cond_value)

	table=sqlite3.connect(dbname)
	cur=table.cursor()
	table.text_factory=str


	return np.array(row_read(command,cur))
	
	
	
	
def read_from_db_all(col_name,dbname,tablename,cond_name,cond_value):

	command='SELECT '+col_name+' FROM '+tablename+' WHERE '+cond_name+'='+str(cond_value)

	table=sqlite3.connect(dbname)
	cur=table.cursor()
	table.text_factory=str


	return np.array(row_read_all(command,cur))
	
	
	
	
	
def read_6D_coordinates_for_specific_turn(dbname,tablename,nturn):
	
	c6d={}
	
	c6d['partID']=read_from_db('partID',dbname,tablename,'turnID',nturn)
	#c6d['cd']=read_from_db('cd',dbname,tablename,'turnID',nturn)
	c6d['x']=read_from_db('x',dbname,tablename,'turnID',nturn)
	c6d['xp']=read_from_db('xp',dbname,tablename,'turnID',nturn)
	c6d['y']=read_from_db('y',dbname,tablename,'turnID',nturn)
	c6d['yp']=read_from_db('yp',dbname,tablename,'turnID',nturn)
	c6d['sig']=read_from_db('sig',dbname,tablename,'turnID',nturn)
	c6d['delta']=read_from_db('delta',dbname,tablename,'turnID',nturn)
	c6d['energy']=read_from_db('energy',dbname,tablename,'turnID',nturn)
	
	return c6d
