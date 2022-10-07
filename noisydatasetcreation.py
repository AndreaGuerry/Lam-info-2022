from funzioni import cicloalgo
import keras
from keras import layers
import tensorflow as tf
import numpy

dataset=[]
tot=3
x=0
while x<tot:
    dataset.append(cicloalgo.cycle(x))
    x=x+1
npds=numpy.array(dataset)
numdataset=numpy.array(dataset)
numpy.save("risultati/datasetnoisy/ds{}.npy".format(tot), numdataset)