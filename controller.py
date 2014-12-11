#---------------------------------------------------------------------------------------------------------
# SIMULATIONS MAIN CONTROLLER
# GIOVANNA CAMPOGIANI
# LAST MODFIIED: 9/12/2014
# --------------------------------------------------------------------------------------------------------------

import sys

sys.path.append("/afs/cern.ch/work/g/gcampogi/public/distributions_tracking/tracking_tools/")

#-----------------------------------------------------------------------------------------------------------------
# LIBRARIES
#-----------------------------------------------------------------------------------------------------------------

from sixtrack_input_generator import launch_madx_and_prepare_sixtrack_input
from simulations_launcher import simulations_launcher_func
from data_storage import data_storage_func
from post_processing import activate_post_processing

import numpy as np
#-----------------------------------------------------------------------------------------------------------------
# USER INPUT BLOCK
#-----------------------------------------------------------------------------------------------------------------





#------- mad-X

mask_file = 'jobref503_withbb_coll'

bunch_charge 	= 10e11

seed 			= 1


# ------ optics
ip = 1

beta_star = 0.55 	# [m] 

beta_stary = beta_star 	#[m]

alpha_x = 0.0 		# [m^-1]

alpha_y = alpha_x 	#[m^-1]


#------- beam

epsilon_n = 3.75e-6 	# [m*rad]

energy0  =  7000000.0 	# MeV

iamp = 9.0 		# in sigma units

eamp = 10.0 		# in sigma units





#-------- distribution

n_samples =  60.0 #10080.0 #MUST BE AN INTEGER MULTIPLE OF n_parts

n_parts = 60.0

main_folder = 'ip%d_seed%d_uniform' %(ip,seed)





#------- SixTrack

wr_fr = 1000.0

SixTrack_folder  =  '/afs/cern.ch/group/si/slap/bin/sixdesk/exes/SixTrack_pro'

forts_folder  =  '$MYWORK/distributions_tracking/sixinput/ip' + str(ip) + '_seed' + str(seed)

fort_n_list  =  [2,8,16] #fort.3 gets automatically created, no need to include it in the list

folder_name = "particleset_"






#------- dB

tablename = 'tracking_data' # DON'T MODIFY

dbschema = 'partID, turnID, cd, pdist, x, xp, y, yp, sig, deltap, energy'

dbname = 'ip%d_seed%d_samples%d-maxampl%d.db' %(ip,seed,int(n_samples),int(eamp))



#-----------------------------------------------------------------------------------------------------------------
# BODY
#-----------------------------------------------------------------------------------------------------------------





#launch_madx_and_prepare_sixtrack_input(mask_file,seed,ip,bunch_charge,fort_n_list)





#simulations_launcher_func(epsilon_n,energy0,deltap0,ip,sig0,iamp,eamp,n_samples,n_parts,wr_fr,SixTrack_folder,forts_folder,fort_n_list,main_folder,folder_name,beta_star,beta_stary,alpha_x,alpha_y)





#data_storage_func( n_samples,n_parts,wr_fr,folder_name, dbname, tablename, main_folder)

clos_orb = np.zeros(6)
clos_orb[3]= yp0

activate_post_processing(dbname, tablename, dbschema, epsilon_n, energy0, iamp, eamp, n_samples,wr_fr, clos_orb,beta_star,beta_stary,alpha_x,alpha_y)
