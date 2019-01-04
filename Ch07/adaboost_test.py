import adaboost
import numpy
from numpy import *

datMat,classLabels=adaboost.loadSimpData()
D=mat(ones((5,1))/5)
#print D
#print adaboost.buildStump(datMat,classLabels,D)
classifierArray=adaboost.adaBoostTrainDS(datMat,classLabels,9)