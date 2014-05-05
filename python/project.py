from mpl_toolkits.mplot3d import Axes3D
import skimage.io as io
from skimage.color import rgb2gray

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import pylab
import scipy as sp

import radec2altaz as ra

# erlaube Erzeugen statischer Variablen
def static_var(varname, value):
    def decorate(func):
        setattr(func, varname, value)
        return func
    return decorate


# formatierte Ausgabe von Arrays
def print_array(_stars):
    for element in _stars:
        print(element)


# Prüfe, ob Element bereits in einem Cluster vorhanden ist
def in_cluster(element, cluster):
    # print("überprüfe cluster:", cluster)
    for sub_cluster in cluster:
        for line in sub_cluster:
            if(element==line):
                # print(element, "ist in sub_cluster")
                return True
    # print(element, " nicht gefunden")
    return False


# fügt alle Nachbarpixel rekursiv in ein neues Cluster ein
def add_neighbors_to_cluster(array, x, y, sub_cluster, value):
    # print("Teste ob Pixel selbst bereits im cluster ist: ")
    if(in_cluster([x,y],cluster)):  # prüfe ob Pixel selbst bereits im array ist
        # print("pixel gibt es schon")
        return
    else:
        # print("Pixel gibt es noch nicht, hänge Pixel ["+ str(x) + ", " + str(y) + "] an")
        sub_cluster.append([x,y])
        # print("überprüfe Nachbarn: ")
        for i in range(-1,2):
            for j in range(-1,2):
                if(i+j == 1 or i+j ==-1):
                    # print("Teste Nachbar: [" + str(x+i) + "," + str(y+j) + "]:")
                    if(x+i < 0 or y+j<0 or x+i>=array.shape[0] or y+j>=array.shape[1]):
                        pass
#                        print("Nachbar leider außerhalb der Bildgrenzen")
                    else:
                        if(array[x+i,y+j] > value):
                            pass
#                            print("Nachbar ist hell genug, hänge an sub_cluster an")
                            add_neighbors_to_cluster(array, x+i, y+j, sub_cluster, value)
                        else:
                            pass
#                            print("Nachbar ist zu dunkel, fahre fort")
#        print("Alle Nachbarn überprüft. Gehe zum nächsten Pixel")
#        print("aktuelles Cluster: ",cluster,"\n")


# testet einen Pixel auf ihren Helligkeitswert und fügt sie ggf. in ein Cluster ein
def test_pixel(img, cluster):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if(img[i,j] != 1):
                pass
            else:
                pass
#                print("\npixel: [" + str(j) +","+ str(i)+ "] ist hell genug")
                if(in_cluster([i,j],cluster)):
                    pass
#                    print("aber pixel bereits im cluster")
                else:
                    cluster.append([])
#                    print("cluster erweitert: " + str(cluster))
                    add_neighbors_to_cluster(img, i, j, cluster[len(cluster)-1], value)


def merge_stars(cluster):
    x,y,cnt=0,0,0
    for i, sub_cluster in enumerate(cluster):
        for pixel in sub_cluster:
            x+=pixel[0]
            y+=pixel[1]
            cnt+=1
#        if(cnt>20):
#            print("zu großer Stern gefunden: ",[x/cnt,y/cnt,cnt**.5])
#            cluster[i]=[0,0,0]
#        else:
            cluster[i]=[x/cnt,y/cnt,cnt**.5]
        x,y,cnt=0,0,0

# beschneidet bild, ändert kontrast, erstellt threshold
def threshold(image,value):
    pass
    image=np.array(np.gradient(image))
    image=image[0,:,:]+image[1,:,:]
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            pass
            if((i-240)**2+(j-320)**2>250**2):
                image[i,j]=0
            else:
                if(image[i,j]<0):
                    image[i,j]*=0
                image[i,j]=image[i,j]**2
                if(image[i,j]>value):
                    pass
                    image[i,j]=1
    return image

# erzeuge einfaches Beispielbild zum Testen
def sample_array():
    img=np.zeros((5,5))
    for i in range(1,3):
        for j in range(2,4):
            img[i,j]=1
    img[0,0]=1
    img[4,4]=1
    return img

# gibt das Bild formatiert mit Markierungen aus
def draw(img, stars, predict, border):
    fig = plt.figure()
    # ax = fig.add_subplot(111,aspect='equal')
    fig = plt.gcf()
    if(stars==1):
        for star in cluster:
            fig.gca().add_artist(plt.Circle((star[1],star[0]),star[2],color='r',fill=False))
    if(predict==1):
        xy=ra.catalog2xy()
        for star in xy:
            print(star)
            fig.gca().add_artist(plt.Circle((star[0],star[1]),2,color='g',fill=False))

    if(border==1):
        fig.gca().add_artist(plt.Circle((320,240),250,color='w',fill=False))
    plt.imshow(img,cmap=pylab.gray())
    plt.show()


print("\n\n\n################################")
print("starting")
print("################################")

cluster=[]
# value=0.95
# value=0.22
value=0.012
value=0.002


print_img=img = io.imread('1.jpg')
img=rgb2gray(img)
img=threshold(img,value)

# Nutze Testbild
# img=print_img=sample_array()

test_pixel(img,cluster)
merge_stars(cluster)
print(len(cluster)," Sterne gefunden.")


draw(print_img,stars=0,predict=1,border=1)
# draw(img,stars=1,predict=1,border=1)
