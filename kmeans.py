# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 00:45:00 2019

@author: shlakhanpal
"""
import scipy.io
import numpy as np
import matplotlib.pyplot as plt
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

plt.plot(X[:, 0], X[:, 1], 'go')
plt.plot(initial_centroids[:, 0], initial_centroids[:, 1], 'rx')

print("X first row ", X[0])

dist = np.zeros((K,num_points))
# comparision here checking the values of the inital centroids and new centroids
# find min distance and then puts it in the coreesponding centroid array
# find average of the centroid arrays and then puts the position of the centroids in that location
# change the value of the centroid
# put the values in the inital centroid into the new centroids and then  start comparision





