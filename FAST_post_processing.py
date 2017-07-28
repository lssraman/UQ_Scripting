import numpy as np
import pandas as pd
import os

# Create a dtype with the binary data format and the desired column names
dt = np.dtype()
data = np.fromfile('P:\UQ\UQ_Scripting\Row_0_BIN_1\FAST'+os.sep+'FAST_row_0_seed_0.outb', dtype=dt)
df = pd.DataFrame.from_records(data)
names = 'count', 'avg', 'scale'

# note that the offsets are larger than the size of the type because of
# struct padding
offsets = 0, 8, 16
formats = 'i4', 'f8', 'f4'
dt = np.dtype({'names': names, 'offsets': offsets, 'formats': formats},
              align=True)
df = DataFrame(np.fromfile('binary.dat', dt))