#-----------------------------------------------------------------------------------------------------------------
# LIBRARIES
#-----------------------------------------------------------------------------------------------------------------

import datetime

from plot_results_module2 import post_processing_func





#-----------------------------------------------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------------------------------------------

def activate_post_processing(dbname,tablename,dbschema,epsilon_n,energy0,iamp,eamp,main_folder,wr_fr,ip,seed):


	
	
	
	start_time = datetime.datetime.now().time()
	
	print '======= START OF THE POSTPROCESSING UTILITY ======'
	
	
	
	
	
	post_processing_func(dbname, tablename, dbschema, epsilon_n, energy0, iamp, eamp, main_folder,wr_fr,ip,seed)
	
	
	
	
	
	end_time = datetime.datetime.now().time()
	
	print 'The program started at ',start_time,' and ended at',end_time
	
	
	
	
	
	print '\n ======= END OF POSTPROCESSING ====== \n\n'
	
