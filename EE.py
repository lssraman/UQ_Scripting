import numpy as np
import os
import shutil
from distutils.dir_util import copy_tree
import pandas as pd
from sobol_seq import i4_sobol,i4_sobol_generate
from turbsimInputs_8ms import write_input_file
from Velocity_spectrum_8ms import turb_specs
from Wind_profile_8ms import write_wind
from FAST_Files.fast_file_generator import write_fast_files
# Python Script for turbsim wind file generation

lowers_BIN1 = np.array([-1.5,-25, 5,  2,   2,     0.05,0.02,0.03,1.5,1.7, 2, 0.00,    0,     0,0,-3.5,-4.5,-2.7])
uppers_BIN1 = np.array([ 3.3, 50,1000,1000, 650,   7.2,7.4, 4.5, 26, 18, 17, 0.08,4.5e-3,0.011,1, 0.5, 6.0, 1.0])

lowers_BIN2 = np.array([-0.4,-10, 8,     2,   2, 0.2,0.05,0.05,1.5,1.7,  2,    0,    0,     0,   0,-3.5,-4.5,-2.7])
uppers_BIN2 = np.array([ 0.9, 50,1400,1300, 450, 7.3,8.1,  4.3, 26, 18, 17, 0.08,3.0e-3,6.0e-3,  1, 0.5, 6.0, 1.0])


lowers_BIN3 = np.array([-0.4,-10, 25,  2,     2,  0.2,0.18, 0.15,1.5,1.7,  2, 0,    0,     0,     0,-3.5,-4.5,-2.7])
uppers_BIN3 = np.array([ 0.7, 25,1600,1500, 650,   7.4,7.3, 4.2,  26, 18, 18, 0.05,2.5e-3,6.5e-3, 1, 0.5, 6.0, 1.0])
#sobols = i4_sobol_generate(19, 20)
sobols=(pd.read_csv('Sobol_set.csv', sep=r'\s+', header=None))
sobols=sobols.values

deltas = pd.read_csv('./deltas.csv', sep=r'\s+', header=None).values


descaled_sobols_BIN1 = sobols.copy()
descaled_sobols_BIN2 = sobols.copy()
descaled_sobols_BIN3 = sobols.copy()
for i in range(len(sobols[0,:])): 
    descaled_sobols_BIN1[i,:] = lowers_BIN1 + (uppers_BIN1 - lowers_BIN1) * descaled_sobols_BIN1[i,:]
    descaled_sobols_BIN2[i,:] = lowers_BIN2 + (uppers_BIN2 - lowers_BIN2) * descaled_sobols_BIN2[i,:]
    descaled_sobols_BIN3[i,:] = lowers_BIN3 + (uppers_BIN3 - lowers_BIN3) * descaled_sobols_BIN3[i,:]

descaled_matrixes = {1:descaled_sobols_BIN1, 2:descaled_sobols_BIN2, 3:descaled_sobols_BIN3}
  
#source='5MW_reference'
#dest = str(os.getcwd())

#copy_tree(source,dest)
#name3='Random_seeds'
#os.makedirs(name3)

for b in range(1,4):
     for ROW in range (0, 20):
	    for COL in ["FLAG"] + range(len(deltas[ROW])):
		name1='Random_seeds'+'/'+'Row_'+str(ROW)+'_BIN_'+str(b) +'/'+'Turbsim_inputs'
		name2='Random_seeds'+'/'+'Row_'+str(ROW)+'_BIN_'+str(b) +'/'+'FAST'
		print 'Generating Turbsim and FAST input files for BIN:'+str(b)+' and Row:'+str(ROW)
                Matrix = descaled_matrixes[b].copy()
		if COL != "FLAG": Matrix[ROW][COL] = lowers_BIN1[COL] + (uppers_BIN1[COL] - lowers_BIN1[COL]) * deltas[ROW][COL]
                #pd.DataFrame(Matrix).to_excel('test.xlsx') ; quit()
		if not os.path.exists(name1):
			os.makedirs(name1)
			os.makedirs(name2)
		else:
			shutil.rmtree(name1)
			shutil.rmtree(name2)
			os.makedirs(name1)
			os.makedirs(name2)
		write_input_file(Matrix[ROW], ROW, COL, b)
		turb_specs(Matrix[ROW], ROW, COL, b)
		write_wind(Matrix[ROW], ROW, COL, b)
		write_fast_files(Matrix[ROW], ROW, COL, b)

print 'File generation complete'


