import os
def write_input_file(vect, ii, jj, randseed=20393):
    orig = open('TurbSim_UsrSpec_8ms.inp', 'r')
    name='Turbsim_Files' + os.sep + 'Turbsim_input_file_8ms_row_'+str(ii)+'_col_' + str(jj)+'.inp'
    
    newf = open(name, 'w')
    # Values for SCMod1 to PCvW  are read from the last 10 columns of the sobol matrix)
    # YY.inp is another file that is created by reading data from columns 3 through 8 of the sobol matrix'
    # XX.profiles is a profile file that is created by reading data from columns 2 through 3 of the sobol matrix'
    #change = {'URef': vect[0], 'UserFile' : '"Turbsim_Files' + os.sep + 'Turbulence_row_%i_col%i'%(ii, jj) + '.inp"', 'ProfileFile': '"Turbsim_Files'+os.sep+'Sobol_row' + str(ii) + '_col' + str(jj) + '.fst"', 'SCMod1': '"GENERAL"', 'SCMod2': '"GENERAL"', 'SCMod3':'"GENERAL"', 'InCDec1': [vect[-10], vect[-7]], 'InCDec2': [vect[-9], vect[-6]], 'InCDec3': [vect[-8], vect[-5]], 'CohExp': vect[-4], 'PC_UW': vect[-3], 'PC_UV': vect[-2], 'PC_VW': vect[-1], 'RandSeed1':randseed}
    change = {'UserFile' : '"Turbsim_Files' + os.sep + 'Turbulence_row_%i_col%i'%(ii, jj) + '.inp"', 'ProfileFile': '"Turbsim_Files'+os.sep+'Sobol_row' + str(ii) + '_col' + str(jj) + '.fst"', 'SCMod1': '"GENERAL"', 'SCMod2': '"GENERAL"', 'SCMod3':'"GENERAL"', 'InCDec1': [vect[-10], vect[-7]], 'InCDec2': [vect[-9], vect[-6]], 'InCDec3': [vect[-8], vect[-5]], 'CohExp': vect[-4], 'PC_UW': vect[-3], 'PC_UV': vect[-2], 'PC_VW': vect[-1], 'RandSeed1':randseed}
    for line in orig.readlines():
       for key in change:
          if key in line:
              if type(change[key]) == list:
                  newline = ' '.join(['"'] + [str(s) for s in change[key]] + ['"'] + line.split(' ')[2:])
                  break
              newline = ' '.join([str(change[key])] + line.split(' ')[1:])
              if line[0]=='"' and line.split(' ')[0][-1]!='"':
              	newline ='"'+newline
              break
       else: newline = line
       newf.write(newline)
    newf.close()
    orig.close()
