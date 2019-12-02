import numpy as np
size = 999
A = np.random.randint(2, size=(size,size))
np.savetxt('in.txt', A, fmt="%d")

with open('in.txt', 'r') as original: data = original.read()
with open('in.txt', 'w') as modified: modified.write(str(size) + "\n" + data)