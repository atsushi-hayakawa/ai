import numpy as np
import cupy as cp
import time
import matplotlib.pyplot as plt

np_start = time.time()
np_x = np.random.normal(50, 10, 10000)
plt.hist(np_x, bins=100)
np_process_time = time.time() - np_start

cp_start = time.time()
cp_x = cp.random.normal(50, 10, 10000)
plt.hist(cp_x.get(), bins=100)
cp_process_time = time.time() - cp_start

print(str(np_process_time))
print(str(cp_process_time))
