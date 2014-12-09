#-----------------------------------------------------------------------------------------------------------------
# LIBRARIES
#-----------------------------------------------------------------------------------------------------------------

import datetime

from plot_results_module2 import post_processing_func





#-----------------------------------------------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------------------------------------------

def activate_post_processing( dbname, 
								tablename, 
								dbschema, 
								emitn, 
								energy0, 
								iamp, eamp,n_samples,wr_fr, closorb,
								beta_star,beta_stary,alpha_x,alpha_y,
								):


	
	
	
	start_time = datetime.datetime.now().time()
	
	print '======= START OF THE POSTPROCESSING UTILITY ======'
	
	
	
	
	
	post_processing_func(dbname, tablename, dbschema, emitn, energy0, iamp, eamp, n_samples,wr_fr, closorb,beta_star,beta_stary,alpha_x,alpha_y)
	
	
	
	
	
	end_time = datetime.datetime.now().time()
	
	print 'The program started at ',start_time,' and ended at',end_time
	
	
	
	
	
	print '\n ======= END OF POSTPROCESSING ====== \n\n'
	
