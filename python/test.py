import astropy.io.ascii as io
import pprint
import numpy as np

def print_deg(position):
    deg=int(position)
    m=int((position%1)*60)
    s=int((position*3600)%60)
    print(deg,'° ',m,'\' ',s,'\'\'')

data=io.read('myfile', format='no_header',delimiter=';')
h=(data['col2'][0])
m=(data['col3'][0])
s=(data['col4'][0])

rec=np.pi*(h+m/60+s/3600)/12  # /2

h=(data['col6'][0])
m=(data['col7'][0])
s=(data['col8'][0])

dec=np.pi*(h+m/60+s/3600)/180  # /2

time=06.245556*np.pi/12
time=7.7566667*np.pi/12
# time=08.053889*np.pi/12
# time=07.182778*np.pi/12
# time=10.059444*np.pi/12
# time=12.065*np.pi/12
# time=14.053611*np.pi/12
# time=16.141667*np.pi/12
# time=19.146944*np.pi/12
# time=21.089444*np.pi/12
# time=18.212778*np.pi/12
# time=14.053611*np.pi/12
time=17.7838889*np.pi/12
# time=01.100556*np.pi/12
geo=90/180*np.pi


time*=1.00278
azimut=180+np.arctan2(np.cos(dec)*np.sin(time-rec),(np.cos(dec)*np.sin(geo)*np.cos(time-rec)-np.sin(dec)*np.cos(geo)))/np.pi*180
altitude=np.arcsin(np.cos(dec)*np.cos(geo)*np.cos(time-rec)+np.sin(dec)*np.sin(geo))/np.pi*180

print_deg(azimut)
print_deg(altitude)
