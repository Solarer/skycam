from mpl_toolkits.mplot3d import Axes3D
import skimage.io as io
from skimage.color import rgb2gray

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

y=640
x=480
pixel=10

img = io.imread('cam.jpg')
img_g=rgb2gray(img)
img_m=np.zeros((48,64))

fig = figure()
ax = Axes3D(fig)
Y = np.arange(0, x/pixel, 1)
X = np.arange(0, y/pixel,1)
X, Y = np.meshgrid(X, Y)

i=j=0
while i < x/pixel :
    while j < y/pixel :
        img_m[i,j]=img_g[i*pixel,j*pixel]
        j+=1
    i+=1
Z = img_m
print(img_g.shape)
print(img_m.shape)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.hot)
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=cm.hot)
ax.set_zlim(-2,2)

pylab.show()
