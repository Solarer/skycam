# Lese Bright-Star-Catalogue ein und erzeuge neue Tabelle, die nur
# ID,Declination, Rectazension und Vmag enthält. Dabei wird nach Objekten
# gefiltert, deren Vmag-Helligkeit mindestens 'value' ist.

import astropy.io.ascii
import numpy as np

Katalog='catalog'       # Datei-Name des Kataloges (Bright-Star-Catalogue)
output='new_catalog'    # Output-File-Name
value=3                 # Auswahlkriterium für Helligkeit

# lese Stern-Katalog in Tabelle 'data' ein und benenne die Spalten wie
# folgt(siehe: names=... )
data = astropy.io.ascii.read(Katalog, names=('ID', '4', '14','25','31','37','44','49','51','60','62','64','69','71','73','Ra_H','Ra_Min','Ra_Sec','Dec_Signum','Dec_H','Dec_Min','Dec_Sec','90','96','Vmag','109','115','121','127','148','154','161','166','170','174','176','180','184','190','194'), format='fixed_width_no_header',col_starts=(0, 4, 14,25,31,37,44,49,51,60,62,64,69,71,73,75,77,79,83,84,86,88,90,96,102,109,115,121,127,148,154,161,166,170,174,176,180,184,190,194),col_ends=(3, 13, 24,30,36,43,48,50,59,61,63,68,70,72,74,76,78,82,83,85,87,89,95,101,106,115,120,126,147,153,160,165,169,173,175,179,183,189,193,198))
f = open(output,'w')

star_cnt=0
for cnt in range(0,len(data)):      # durchlaufe alle Zeilen der Tabelle
    if(data['Vmag'][cnt]>value)or(str(data['Vmag'][cnt])=='--'):    # lasse Zeile aus, falls Objekt zu dunkel oder Wert leer
        continue
    else:           # ansonsten formatiere Zeile so wie gewünscht und schreibe in Datei
        star_cnt+=1
        for title in ['ID','Ra_H','Ra_Min','Ra_Sec','Dec_Signum','Dec_H','Dec_Min','Dec_Sec','Vmag']:
            f.write(str(data[title][cnt]))
            if(title=='ID')or(title=='Ra_Sec')or(title=='Dec_Sec'):
                f.write('; ')
            elif(title!='Dec_Signum')and(title!='Vmag'):
                f.write(':')
            if(title=='Vmag'):
                f.write('\n')
f.close()

print(star_cnt, ' Sterne in neuer Liste mit Helligkeit >',value)
# Entferne letztes '\n' am Ende der Datei, da dieses überflüssig ist
with open(output, 'rb+') as filehandle:
    filehandle.seek(-1, 2)
    filehandle.truncate()
filehandle.close()
