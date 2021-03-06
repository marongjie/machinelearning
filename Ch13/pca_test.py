import pca
from numpy import *
import matplotlib
import matplotlib.pyplot as plt

dataMat=pca.loadDataSet('testSet.txt')
#print dataMat
lowDMat,reconMat=pca.pca(dataMat,1)
#lowDMat,reconMat=pca.pca(dataMat,2)
print shape(lowDMat)
fig=plt.figure()
ax=fig.add_subplot(111)
ax.scatter(dataMat[:,0].flatten().A[0],dataMat[:,1].flatten().A[0],marker='^',s=90)
ax.scatter(reconMat[:,0].flatten().A[0],reconMat[:,1].flatten().A[0],marker='o',s=20,c='red')
plt.show()