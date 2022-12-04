import numpy as np
import matplotlib.pyplot as plt

陣列 = np.zeros([10,10])
陣列 = 陣列.astype('uint8')

for x in range(10) :
    for y in range(10) :
        陣列[y, x] = 255 - 25* y - 25* x               
    
plt.imshow(陣列, cmap='gray', vmin=0, vmax=255)
plt.colorbar()
plt.show()

