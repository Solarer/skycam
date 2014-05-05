import ephem
import numpy as np

def catalog2xy():
    # Lese Tabelle in Liste 'data'
    f=open('new_catalog')
    inp=f.read()
    data=[]
    file=inp.split('\n')
    for line in file:
        data.append(line.split(';'))
    # print(data)

# Setzte Beobachter
    me = ephem.Observer()
    me.long = ephem.degrees('-17:52:34.00')
    me.lat = ephem.degrees('28:45:34.00')
    me.date = '2014/05/02 12:00:29'
    me.pressure=0

# Initialisiere Stern
    star = ephem.FixedBody()

# Berechne für jeden Stern die neuen Koordinaten und gebe sie zurück
    xy=[]
    for line in data:
        eq = ephem.Equatorial(line[1],line[2],epoch=ephem.J2000)
        star._ra = eq.ra
        star._dec = eq.dec
        star.compute(me)

        x=(-3.34905*star.alt+299.623)*np.cos((star.az-237)*3.1415926/180)+328.2
        y=-(-3.34905*star.alt+299.623)*np.sin((star.az-237)*3.1415926/180)+252.9

        # print('Azimuth: ',star.az,'Altitude: ', star.alt)
        # print('x: ',x,'y: ', y)
        if(x>0)and(y>0)and(x<640)and(y<480):
            xy.append([int(x+0.5),int(y+0.5)])

    return xy
    f.close()

print(catalog2xy())
