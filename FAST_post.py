import numpy as np
import matplotlib.pyplot as plt

myarray = np.loadtxt('C:\Users\lsethura\OPENMDAO\UQ_Scripting\Row_0_BIN_1\FAST\Sobol_row0_seed_0.out',skiprows=8)
y = myarray.astype(np.float)
fig, ax = plt.subplots(nrows=2,ncols=2)

plt.subplot(2,2,1)
plt.plot(y[:,0],y[:,8],'b--')
plt.xlabel('Time')
plt.ylabel('Mxb1(kNm)')

plt.subplot(2,2,2)
plt.plot(y[:,0],y[:,11],'r--')
plt.xlabel('Time')
plt.ylabel('Myb1(kNm)')

plt.subplot(2,2,3)
plt.plot(y[:,0],y[:,14],'g--')
plt.xlabel('Time')
plt.ylabel('Mzb1 (kNm)')

plt.subplot(2,2,4)
plt.plot(y[:,0],y[:,19],'k--')
plt.xlabel('Time')
plt.ylabel("Torque (kNm)")
plt.show()

savefig('FAST.png', facecolor=fig.get_facecolor(), transparent=True)


plt.show()

