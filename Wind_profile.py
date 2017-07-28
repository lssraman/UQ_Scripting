import numpy as np
import os
import decimal
import pandas
from collections import OrderedDict

def write_wind(invec, ii, jj):

    Height=(np.array([np.arange(27,154)],dtype=decimal.Decimal))
    
    V_ref=invec[0]
    alpha=invec[1]
    Beta=invec[2]
    Z_hub=90.
    
    new_Height=(Height/Z_hub).T
    
    Height=(np.array([np.arange(27,154)])).T
    a=len(Height)
    print a 
    
    U=np.zeros((a,1),dtype=float)
    Beta1=np.zeros((a,1),dtype=float)
    
    
    for i in range(0,a):
    	U[i,0]= V_ref*(new_Height[i,0])**alpha
    	Beta1[i,0]= 90+(Beta/63)*(Height[i,0])-90*(Beta/63)
    
    
    df=pandas.DataFrame(OrderedDict({'Height (m)':Height[:,0],'Wind speed (m/s)': U[:,0],'Wind --Direction--(deg, cntr-clockwise )': Beta1[:,0]}))
    
    name=os.sep.join(['Turbsim_Files', 'Sobol_row' + str(ii) + '_col' + str(jj) + '.profiles'])
    with open("UsrShear.profiles",'r') as f:
    	get_all=f.readlines() 
    	
    with open(name,'w') as f:
    	for i,line in enumerate(get_all,1):
    		if i < 12:  
    			f.writelines(line)
    		else: 
    			f.write(df.to_string(index=False,header=False,col_space=7))
    			break
