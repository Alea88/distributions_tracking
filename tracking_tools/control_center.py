#---------------------------------------------------------------------------------------------------------
# TAIL EVOLUTION STUDIES CONTROLLER
# GIOVANNA CAMPOGIANI
# LAST MODFIIED: 26/09/2014
# --------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------
# LIBRARIES
#-----------------------------------------------------------------------------------------------------------------

from simulations_launcher import simulations_launcher_func
from data_storage import data_storage_func
from post_processing import activate_post_processing
import numpy as np

#-----------------------------------------------------------------------------------------------------------------
# USER INPUT BLOCK
#-----------------------------------------------------------------------------------------------------------------





#------- mad-X

mask_file = 'nomLHC_withbb_coll'

bunch_charge 	= 10e11

seed 			= 1

beta_star = 0.55 	# [m] 

beta_stary = beta_star 	#[m]

alpha_x = 0.0 		# [m^-1]

alpha_y = alpha_x 	#[m^-1]


#------- beam

epsilon_n = 3.75e-6 	# [m*rad]

energy0  =  7000000.0 	# MeV

deltap0  =  0.0 	# []

yp0  =  0.0		#[mrad]

xp0  =  0.0		# [mrad]

sig0  =  0.0 		# []

iamp = 0.0 		# in sigma units

eamp = 10.0 		# in sigma units





#-------- distribution

n_samples =  10080.0 #MUST BE AN INTEGER MULTIPLE OF n_parts

n_parts = 60.0

main_folder = 'uniform'





#------- SixTrack

wr_fr = 1000.0

SixTrack_folder  =  '/afs/cern.ch/group/si/slap/bin/sixdesk/exes/SixTrack_pro'

forts_folder  =  '$MYWORK/sixtrack_input/ip1'

fort_n_list  =  [2,3,8,16]

folder_name = "particleset_"






#------- dB

tablename = 'tracking_data' # DON'T MODIFY

dbschema = 'partID, turnID, cd, pdist, x, xp, y, yp, sig, deltap, energy'

dbname = 'ip1_%d_%s.db' %(int(n_samples),str(eamp))



#-----------------------------------------------------------------------------------------------------------------
# BODY
#-----------------------------------------------------------------------------------------------------------------





#sixtrack_input_generator()





#simulations_launcher_func(epsilon_n,energy0,deltap0,xp0,yp0,sig0,iamp,eamp,n_samples,n_parts,wr_fr,SixTrack_folder,forts_folder,fort_n_list,folder_name,beta_star,beta_stary,alpha_x,alpha_y)






#data_storage_func( n_samples,n_parts,wr_fr,folder_name, dbname, tablename, main_folder)


activate_post_processing(dbname, tablename, dbschema, epsilon_n, energy0, iamp, eamp, n_samples,wr_fr, np.zeros(6),beta_star,beta_stary,alpha_x,alpha_y)
