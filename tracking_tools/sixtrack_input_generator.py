#---------------------------------------------------------------------------------------------------------
# SIXTRACK INPUT GENERATOR
# GIOVANNA CAMPOGIANI
# LAST MODFIIED: 9/12/2014
# Generates SixTrack input files from MadX mask file
# --------------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------------
# LIBRARIES
#-----------------------------------------------------------------------------------------------------------------

import numpy as np
import os
import datetime
import subprocess

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

	os.makedirs('madxinput/ip%d_seed%d' %(IP,SEEDRAN))
	os.system('mv madxinput/%s.mask madxinput/ip%d_seed%d' %(new_mask_name,IP,SEEDRAN))
	
	print 'The mask file',mask_name,'.mask has been updated with the user input data.'
	print 'The new mask file name is: ',new_mask_name,'.mask'
	
	return new_mask_name





def launch_madx(mask_name, ip, seed):
	'''to generate the SixTrack input file from the mask
	'''
	mask_file=mask_name+'.mask'
	home=os.environ['PWD']
	madxfolder = 'madxinput/ip' + str(ip) + '_seed' + str(seed)
	os.chdir(madxfolder)
	print 'Working directory changed to ',os.getcwd()
	print datetime.datetime.now().time(),': Launching MADx', mask_name
	
	out=open('log_%s.log'%mask_name,'wb')
	err=open('err_%s.log'%mask_name,'wb')
	proc_stat=subprocess.Popen('madx %s' %mask_file, shell=True,
                        #stdin=subprocess.PIPE,
                        stdout=out,
                        stderr=err,
                        )
	proc_stat.wait()

	print datetime.datetime.now().time(),': MADx run. Returning to home directory.'
	os.chdir(home)
	
	return madxfolder


	
def integratefc3 (madxfolder, sixfolder):

	os.makedirs('%s' %sixfolder)

	with open('%s/fc.3' %madxfolder, 'r') as f:
	     	fc_data = f.read()
	f.close()

	f_old = open("sixinput/fort.3.mother")	
	f_new = open("%s/fort.3" %sixfolder, "wb")

	for line in f_old:
		if 'INSERT MULT DATA HERE' in line:
			line = fc_data
		f_new.write(line)


	f_old.close()
	f_new.close()
	
	os.system('cat %s/fort.3' %sixfolder)
	
	print 'Fort.3 successfully created'


	
def makeforts(madxfolder, sixfolder, files_list):

	for n in files_list:
		os.system('mv %s/fc.%d %s/fort.%d' %(madxfolder,n,sixfolder,n))
	
	os.system('ls %s' %sixfolder)
	
	print 'SixTrack input files creation completed'

#-----------------------------------------------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------------------------------------------

def launch_madx_and_prepare_sixtrack_input(mask_file,seed,ip,bunch_charge,files_list):


	start_time = datetime.datetime.now().time()
	
	
	
	print '======= GENERATING SIXTRACK INPUT FILES 2,3,6,8 ======'
	
	
	
	
	print 'If assertion error: user must provide with the mask file in madxinput folder'
	assert os.path.exists('./madxinput/%s.mask' %mask_file)		#check that mask file is in madxinput directory
	print mask_file,' correctly found in the mask folder'
	
	
	
	
	print 'If assertion error: user must provide with the fort.3.mother file in sixinput folder'
	assert os.path.exists('./sixinput/fort.3.mother')			#check that fort.3.mother is in sixinput directory
	print 'fort.3.mother correctly found in the mask folder'
	
	
	
	print 'Next step: update the mask file with the user defined IP, SEED and BUNCH CHARGE values'
	new_mask_file = update_mask(bunch_charge,seed,ip,mask_file) # substitutes bunch_charge and seed in mask

	
	
	
	print 'Next step: launch MADx'
	madxfolder = launch_madx(new_mask_file,ip, seed)
	
	
	
	
	print 'Next step: integrate fc.3 in the fort.3.mother file'
	sixfolder = 'sixinput/ip' + str(ip) + '_seed' + str(seed)
	integratefc3( madxfolder,  sixfolder)
	
	
	
	
	print 'Next step: rename remaining fc files'
	makeforts(madxfolder, sixfolder, files_list)
	
	
	
	
	end_time = datetime.datetime.now().time()
	print 'The program started at ',start_time,' and ended at',end_time
	
	
	
	
	print '======= END OF SIXTRACK INPUT FILES GENERATOR ======'

