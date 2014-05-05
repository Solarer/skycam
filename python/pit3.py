import skimage.io as io
import matplotlib.pyplot as plt
import numpy as np
from skimage.color import rgb2gray

from skimage.exposure import equalize_hist
###############################################
def show_images(images,titles=None):
    """Display a list of images"""
    n_ims = len(images)
    if titles is None: titles = ['(%d)' % i for i in range(1,n_ims + 1)]
    fig = plt.figure()
    n = 1
    for image,title in zip(images,titles):
        a = fig.add_subplot(1,n_ims,n) # Make subplot
        if image.ndim == 2: # Is image grayscale?
            plt.gray() # Only place in this blog you can't replace 'gray' with 'grey'
        plt.imshow(image)
        a.set_title(title)
        n += 1
    fig.set_size_inches(np.array(fig.get_size_inches()) * n_ims)
    plt.show()
################################################
img = io.imread('cam.jpg')
img_g=rgb2gray(img)

equalized_image = equalize_hist(img_g)

#show_images(images=[img_g,equalized_image],
            titles=["Grayscale","Histogram Equalized"])
gray_image=img_g

import pandas as pd
from ggplot import *

ggplot(pd.DataFrame(),aes(fill=True,alpha=0.5)) + \
    geom_density(aes(x=gray_image.flatten()),color='green') + \
    geom_density(aes(x=equalized_image.flatten()),color='orange') + \
    ggtitle("Histogram Equalization Process\n(From Green to Orange)") + \
    xlab("pixel intensity") + \
    ylab("density")
