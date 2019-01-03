import kMeans
from numpy import *
import matplotlib.pyplot as plt

'''
datMat=mat(kMeans.loadDataSet('testSet.txt'))
print min(datMat[:,0])
print min(datMat[:,1])
print max(datMat[:,1])
print max(datMat[:,0])
print kMeans.randCent(datMat,2)
print kMeans.distEclud(datMat[0],datMat[1])
myCentroids,clustAssing=kMeans.kMeans(datMat,4)
'''
rect=[0.1,0.1,0.8,0.8]
fig=plt.figure()
ax0=fig.add_axes(rect,label='ax0')
imgP=plt.imread('Portland.png')
ax0.imshow(imgP)
plt.show()