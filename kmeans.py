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
iterations = 10
X = np.array(test['X'])
#X = h5py.File('kmeansdata.mat', 'r') # class activity
#X = np.array(Xa)

#print('Printing data in X...')
#print(X)

print('Dimensions of X', X.shape)

num_points = len(X)
print("Total number of points in dataset, ie. X:", num_points)

K = 3 # class activity

initial_centroids = [[3,3],[6,2],[8,5]]
old_centroids = [[0,0],[0,0],[0,0]]

print("X first row ", X[0])

dist = np.zeros((K,num_points))
cent1_min = []
cent2_min = []
cent3_min = []

marker_style = dict(color='tab:blue', linestyle=':', marker='o', markersize=15, markerfacecoloralt='tab:red')

# plot initial data
for x,y in X:
    plt.scatter(x,y, color='y')
plt.scatter(initial_centroids[0][0], initial_centroids[0][1], color='r', marker='x')
plt.scatter(initial_centroids[1][0], initial_centroids[1][1], color='g', marker='x')
plt.scatter(initial_centroids[2][0], initial_centroids[2][1], color='b', marker='x')
plt.show()


# number of iterations
for i in range(iterations):
    # range of data
    # calculate value between point and centroid, get min
    # append min into a plot array
    for c in range(len(X)):
        val1 = distance.euclidean(X[c],initial_centroids[0])
        val2 = distance.euclidean(X[c],initial_centroids[1])
        val3 = distance.euclidean(X[c],initial_centroids[2])
        if(min(val1,val2,val3) == val1):
            cent1_min.append(X[c])
        elif(min(val1,val2,val3) == val2):
            cent2_min.append(X[c])
        else:
            cent3_min.append(X[c])
            
    # calculate new centroids
    meanx1 = np.mean(cent1_min,axis=0)
    meanx2 = np.mean(cent2_min,axis=0)
    meanx3 = np.mean(cent3_min,axis=0)
    old_centroids = initial_centroids

    # flush old centroids
    initial_centroids.clear()

    # add new centroids
    initial_centroids.append(meanx1)
    initial_centroids.append(meanx2)
    initial_centroids.append(meanx3)
    print(initial_centroids)
    
    # plot datapoints of each centroidal array r,g,b
    for x,y in cent1_min:
        plt.scatter(x,y, color='r')
    for x,y in cent2_min:
        plt.scatter(x,y, color='g')
    for x,y in cent3_min:
        plt.scatter(x,y, color='b')

    # plot centroids 
    plt.scatter(old_centroids[0][0], old_centroids[0][1], color='r', marker='x')
    plt.scatter(old_centroids[1][0], old_centroids[1][1], color='g', marker='x')
    plt.scatter(old_centroids[2][0], old_centroids[2][1], color='b', marker='x')
    plt.pause(0.05)

    # flush old centroidal array
    cent1_min.clear()
    cent2_min.clear()
    cent3_min.clear()

    # clear plot for next plot
    # dont clear last plot with -1
    if i < iterations-1:
        plt.clf()
# show plot
plt.show()