# Stores the results of SixTrack simulation in an SQlite db

#-----------------------------------------------------------------------------------------------------------------
# LIBRARIES
#-----------------------------------------------------------------------------------------------------------------

import datetime
import os
import sqlite3
from read_fortbin import read_allfortbin

#-----------------------------------------------------------------------------------------------------------------
# LIBRARIES
#-----------------------------------------------------------------------------------------------------------------


def data_to_dictionary(main_folder,folder_name,folder_max_number):
	'''routine that reads all the data and stacks it up in a dedicated dictionary
	'''
	
	tbt_data={} #turn by turn data container
	
	np=60
	
	pID_bias=0
	bunch={}
	for n in range(folder_max_number+1):
		dest_path=os.getcwd()+'/'+main_folder+'/'+folder_name+str(n)
		print dest_path
		head,part=read_allfortbin(pID_bias,basedir='%s' %dest_path)
		pID_bias=np*(n+1)
		print 'pID_bias=',pID_bias
		bunch.update(part)
		print 'the tbt data read for this particle is long',len(part)
		#tbt_data[mad_seed]=bunch
	#tbt_data=bunch
	closo = head['closorb']

	return bunch, closo





def dictionary_to_list(tbt_data,  wr_fr):
	'''translates the dictionary to a list for db insertion
	'''
	table=[]

	for pID in sorted(tbt_data.keys()):
		for tID in range(len(tbt_data[pID])):
			pdist = tbt_data[pID][tID][0]
			x = tbt_data[pID][tID][1]
			xp = tbt_data[pID][tID][2]
			y = tbt_data[pID][tID][3]
			yp = tbt_data[pID][tID][4]
			sig = tbt_data[pID][tID][5]
			delta = tbt_data[pID][tID][6]
			energy = tbt_data[pID][tID][7]
			#cd = gd [pID-1]
			single_entry = (pID, tID*wr_fr, pdist, x, xp, y, yp, sig, delta, energy)
			table.append(single_entry)

	return table





def update_db(dbname, tablename, tbt_data, wr_fr):
	
	tbt = sqlite3.connect(dbname)
	cur = tbt.cursor()
	
	#data insertion in the table block
	table = dictionary_to_list(tbt_data, wr_fr)
	cur.executemany('INSERT INTO tracking_data VALUES(?,?,?,?,?,?,?,?,?,?);',table)
	tbt.commit()
	tbt.text_factory=str
	print ('Data stored in the database %s, table: tracking_data' %dbname)
	
	cur.execute('SELECT * FROM tracking_data;')
	print 'Data successfully stored. Here is the first line of the table:'
	print cur.fetchone()
					
	cur.close()
	tbt.close()
	





def create_db(folder_name,dbname,n_samples,tablename):
	'''the data will be store in table called tracking_data 
	in the file folder_name+n_samples
	'''
	#table creation block
	#dbname = folder_name+str(n_samples)+'_'+str(iamp)+'-'+str(eamp)
	dbschema = 'partID,turnID,pdist,x,xp,y,yp,sig,delta,energy'
	
	tbt = sqlite3.connect('%s' %dbname)
	cur = tbt.cursor()

#	cur.execute('DROP TABLE tracking_data;')
	cur.execute('''
	CREATE TABLE IF NOT EXISTS %s(
		partID INTEGER, 
		turnID INTEGER, 
		pdist REAL,
		x REAL,
		xp REAL,
		y REAL,
		yp REAL, 
		sig REAL,
		delta REAL,
		energy REAL);''' %tablename)
	tbt.commit()
			
	cur.close()
	tbt.close()
	
	return dbschema





def backup_db(dbname,foldername):
	os.system('rfcp %s $CASTOR_HOME/%s' %(dbname,foldername))
	os.system('nsls')
	print 'Database ',dbname,' successfully backed up on CASTOR'
	




def move_db(dbname,dest_fold):
	os.system('cp %s %s' %(dbname,dest_fold))
	os.system('ls')
	print 'Database ',dbname,' successfully moved to ',dest_fold
	




def remove_folder_content(mother_folder):
	os.system('rm -r %s/*' %mother_folder)
	os.system('ls -l %s' %mother_folder)
	print 'All folders contained in ',mother_folder,' successfully removed'





#-----------------------------------------------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------------------------------------------


def data_storage_func(	n_samples,
						n_parts,
						wr_fr,
						folder_name,
						dbname,
						tablename,
						main_folder #uniform
						):


	

	start_time = datetime.datetime.now().time()
	
	print '\n ======= START OF DATA STORAGE UTILITY ====== \n\n'
	
	
	
	
	
	print 'Next step: storing the data in an SQlite db'
	
	i = int(n_samples / n_parts) - 1
	
	tbt_data, closo = data_to_dictionary(main_folder,folder_name, i)
	
	dbschema = create_db(folder_name, dbname, n_samples, tablename)
	
	
	update_db(dbname, tablename, tbt_data, wr_fr)
	
	#backup_db(dbname,main_folder)
	
	print 'Data successfully stored in ', dbname, ' with the following row structure'
	print '(',dbschema,')'
	
	
	
	
	
	#print 'Next step: moving the dB'
	
	#move_db(dbname, '.')
	
	
	
	
	
	#print 'Next step: removing binary files'
	
	#remove_folder_content(main_folder)
	
	
	print 'The closed orbit vector is: ', closo
	
	
	end_time = datetime.datetime.now().time()
	
	print 'The program started at ', start_time, ' and ended at', end_time
	
	
	
	
	
	print '\n ======= END OF DATA STORAGE UTILITY ====== \n\n'
