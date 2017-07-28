import os, sys
import random
from random import randint
import numpy as np
from string import split

def write_input_file(vect, ii, jj,b):

   ll=np.zeros((100,1),dtype=int)
   for n in range(0,100):
       ll[n,0]=500000+n
       if b==1:
            orig = open('\\\monsoon-data\Confidential\UQ\UQ_Scripting\TurbSim_UsrSpec_8ms.inp', 'r')
            c=8
       elif b==2:
            orig = open('\\\monsoon-data\Confidential\UQ\UQ_Scripting\TurbSim_UsrSpec_12ms.inp', 'r')
            c=12
       else:
            orig = open('\\\monsoon-data\Confidential\UQ\UQ_Scripting\TurbSim_UsrSpec_18ms.inp', 'r')
            c=18
       #ll[n,0]=(randint(-2147483648,2147483647))
       name='Random_seeds'+os.sep+'Row_' + str(ii)+'_BIN_'+str(b)+os.sep+'Turbsim_inputs'+os.sep+'Turbsim_input_file_'+str(c)+'ms_row_'+str(ii)+'_seed_'+str(n)+'.inp'
       newf = open(name, 'w')
       change = {'RandSeed1': ll[n,0], 'UserFile' :str(c)+'ms_Turbulence_row_'+str(ii)+'.inp', 'ProfileFile': str(c)+'ms_Sobol_row_'+str(ii)+'.profiles', 'SCMod1': '"GENERAL"', 'SCMod2': '"GENERAL"', 'SCMod3':'"GENERAL"', 'InCDec1': [vect[-10], vect[-7]], 'InCDec2': [vect[-9], vect[-6]], 'InCDec3': [vect[-8], vect[-5]], 'CohExp': vect[-4], 'PC_UW': vect[-3], 'PC_UV': vect[-2], 'PC_VW': vect[-1]}
       for line in orig.readlines():
           for key in change:
               if key in line:
                     if type(change[key]) == list:
                          newline = ' '.join(['"']+[str(s) for s in change[key]]+['"'] + line.split(' ')[2:])
                          break
                     newline = ' '.join([str(change[key])] + line.split(' ')[1:])
                     if line[0]=='"' and line.split(' ')[0][-1]!='"': 
                         newline ='"'+newline
                     break
           else: newline = line
           newf.write(newline)
       newf.close()
       orig.close()
