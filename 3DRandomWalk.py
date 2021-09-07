#author: Ernesto Guzmán Saleh A00824855

import numpy as np
from matplotlib import pyplot as plt

Nsteps=10000
ndim=3

L=1
pos=np.zeros((Nsteps, ndim))

for i in (np.array(range(Nsteps))+1)[0:-1]:
    for j in (np.array(range(ndim))+0):
        step=np.random.randint(low=-1, high=2, dtype=int)*L
        pos[i,j]=pos[i-1, j]+step
    
end=(int(pos[-1,0]), int(pos[-1,1]),int(pos[-1,2]))
start=(int(pos[0,0]), int(pos[0,1]),int(pos[0,2]))

fig=plt.figure()
ax=plt.axes(projection="3d")
ax.xaxis.pane.set_edgecolor('b')
ax.yaxis.pane.set_edgecolor('b')
ax.zaxis.pane.set_edgecolor('b')
ax.plot3D(pos[:,0], pos[:,1],pos[:,2], c="b")
ax.scatter3D(*start, c="m", s=200, label="Start:"+ str(start)) #start
ax.scatter3D(*end, c="r", s=200, label="End:"+ str(end)) #end
plt.legend()
plt.show()

