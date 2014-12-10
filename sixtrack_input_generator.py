


#-----------------------------------------------------------------------------------------------------------------
# LIBRARIES
#-----------------------------------------------------------------------------------------------------------------

import numpy as np
import os
import datetime
import subprocess

#from uniform_distribution import uniform_distribution_generator, write_to_file, calc_sigma, gaussian, gaussian_to_file, initialize_coordinates
#from tracking_launcher import update_mask, launch_madx, assign_idfor, make_folder, copy_SixTrack, copy_forts,launch_jobs
#from data_to_db_2 import data_to_dictionary, create_db, update_db, backup_db, move_db, remove_folder_content
#from read_fortbin import read_allfortbin
#from plot_results_module import post_processing

#-----------------------------------------------------------------------------------------------------------------
# USER INPUT BLOCK
#-----------------------------------------------------------------------------------------------------------------

#------- mad-X

mask_file = 'jobref503_withbb_coll'

bunch_charge 	= 1e11
seed 		= 1
ip = 3
files_list = [2,8,16]

#------- beam

emitn=3.75e-6
energy0  =  7000000.0 #MeV
deltap0  =  0.0 # []
xp0  =  0.0 # [mrad]
yp0  =  0.0 # [mrad]
sig0  =  0.0 # []
iamp = 0.0 # in sigma units
eamp = 10.0 # in sigma units
beta_star = 0.55

#sigma, gamma_rel = calc_sigma(emitn,energy0,beta_star)
#print "sigma = ",sigma

#------- SixTrack

wr_fr = 1000.0


#-----------------------------------------------------------------------------------------------------------------
# UTILITIES
#-----------------------------------------------------------------------------------------------------------------



def update_mask(NPART,SEEDRAN,IP,mask_name):
	'''assumes NPART=bunch_charge, SEEDRAN=seed
	returns the name of a new mask file with the input data substitutes to %SEEDRAN and %NPART
	'''
	
	new_mask_name = mask_name + '_ip' +str(IP) + '_' + str(SEEDRAN)
	
	infile = open('madxinput/%s.mask' %mask_name)
	outfile = open('madxinput/%s.mask' %new_mask_name, 'w')
	
	replacements = {'%NPART':str(NPART), '%SEEDRAN':str(SEEDRAN), '%IP':'IP'+str(IP)}
	
	for line in infile:
		for old,new in replacements.iteritems():
			line = line.replace(old,new)
		outfile.write(line)
	infile.close()
	outfile.close()

	os.makedirs('madxinput/ip%d' %IP)
	os.system('mv madxinput/%s.mask madxinput/ip%d' %(new_mask_name,IP))
	
	return new_mask_name





def launch_madx(mask_name, ip):
	'''to generate the SixTrack input file from the mask
	'''
	mask_file=mask_name+'.mask'
	home=os.environ['PWD']
	madxfolder = 'madxinput/ip' + str(ip)
	os.chdir(madxfolder)
	print 'Working directory changed to ',os.getcwd()
	print datetime.datetime.now().time(),': Launching MADx', mask_name
	#out=open('log_%s.log'%mask_name,'wb')
	#err=open('err_%s.log'%mask_name,'wb')
	proc_stat=subprocess.Popen('madx %s' %mask_file, shell=True,
                        #stdin=subprocess.PIPE,
                        stdout=out,
                        stderr=err,
                        )
	proc_stat.wait()


	#os.system('cp ../../fc.3 .') # test file
	#os.system('cp ../../fc.2 .') # test file
	#os.system('cp ../../fc.8 .') # test file
	#os.system('cp ../../fc.16 .') # test file

	print datetime.datetime.now().time(),': MADx run. Returning to home directory.'
	os.chdir(home)
	
	return madxfolder


	
def integratefc3 (madxfolder, sixfolder):

	os.makedirs('%s' %sixfolder)

	with open('%s/fc.3' %madxfolder, 'r') as f:
	     	fc_data = f.read()
	f.close()

	f_old = open("sixinput/fort.3.mother")	
	f_new = open("%s/fort.3" %sixfolder, "w")

	for line in f_old:
		if 'INSERT MULT DATA HERE' in line:
			line = fc_data
		f_new.write(line)


	f_old.close()
	f_new.close()
	
	os.system('cat %s/fort.3' %sixfolder)

	
def makeforts(madxfolder, sixfolder, files_list):

	for n in files_list:
		os.system('mv %s/fc.%d %s/fort.%d' %(madxfolder,n,sixfolder,n))
	os.system('ls %s' %sixfolder)

#-----------------------------------------------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------------------------------------------
start_time = datetime.datetime.now().time()

print '======= GENERATING SIXTRACK INPUT FILES 2,3,6,8 ======'




print 'If assertion error: user must provide with the mask file in madxinput folder'
assert os.path.exists('./madxinput/%s.mask' %mask_file)		#check that mask file is in madxinput directory
print mask_file,' correctly found in the mask folder'




print 'If assertion error: user must provide with the fort.3.mother file in sixinput folder'
assert os.path.exists('./sixinput/fort.3.mother')			#check that fort.3.mother is in sixinput directory
print 'fort.3.mother correctly found in the mask folder'


new_mask_file = update_mask(bunch_charge,seed,ip,mask_file) # substitutes bunch_charge and seed in mask




print 'The mask file',mask_file,'.mask has been updated with the user input data.'
print 'The new mask file name is: ',new_mask_file,'.mask'



print 'Next step: to launch MADx'

madxfolder = launch_madx(new_mask_file,ip)



print 'Next step: integrate fc.3 in the fort.3.mother file'

sixfolder = 'sixinput/ip' + str(ip)
integratefc3( madxfolder,  sixfolder)



print 'Next step: rename remaining fc files'
makeforts(madxfolder, sixfolder, files_list)

end_time = datetime.datetime.now().time()
print 'The program started at ',start_time,' and ended at',end_time

print '======= END OF SIXTRACK INPUT FILES GENERATOR ======'

