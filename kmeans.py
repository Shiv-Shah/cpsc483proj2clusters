# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 00:45:00 2019

@author: shlakhanpal
"""
import scipy.io
from scipy.spatial import distance
import numpy as np
import matplotlib.pyplot as plt
import math 
#import pandas as pd
#import h5py


test = scipy.io.loadmat('kmeansdata.mat')

X = np.array(test['X'])
#X = h5py.File('kmeansdata.mat', 'r') # class activity
#X = np.array(Xa)
print('Printing data in X...')
print(X)

print('Dimensions of X', X.shape)

num_points = len(X)
print("Total number of points in dataset, ie. X:", num_points)

K = 3 # class activity

initial_centroids = [[3,3],[6,2],[8,5]]
new_centroids = [[0,0], [0,0], [0,0]] # class activity

#plt.plot(X[:, 0], X[:, 1], 'go')
#plt.plot(initial_centroids[:, 0], initial_centroids[:, 1], 'rx')

print("X first row ", X[0])

dist = np.zeros((K,num_points))
cent1_min = []
cent2_min = []
cent3_min = []

for i in range(10000):
    for c in range(len(X)):
        val1 = distance.euclidean(X[c],initial_centroids[0])
        val2 = distance.euclidean(X[c],initial_centroids[1])
        val3 = distance.euclidean(X[c],initial_centroids[2])
        if(min(val1,val2,val3) == val1):
            cent1_min.append(val1)
        elif(min(val1,val2,val3) == val2):
            cent2_min.append(val2)
        else:
            cent3_min.append(val3)
    meanx1 = np.mean(cent1_min,axis=0)
    meanx2 = np.mean(cent2_min,axis=0)
    meanx3 = np.mean(cent3_min,axis=0)
    new_centroids = initial_centroids
    initial_centroids.clear()
    initial_centroids.append(meanx1)
    initial_centroids.append(meanx2)
    initial_centroids.append(meanx3)
    print(initial_centroids)

# comparision here checking the values of the inital centroids and new centroids
# find min distance and then puts it in the coreesponding centroid array
# find average of the centroid arrays and then puts the position of the centroids in that location
# change the value of the centroid
# put the values in the inital centroid into the new centroids and then  start comparision





