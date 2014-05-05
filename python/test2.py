import ephem
telescope = ephem.Observer()
telescope.long = ephem.degrees('0')
telescope.lat = ephem.degrees('90')
telescope.date = '1000/30/04 5:56:54'
star = ephem.FixedBody()
star._epoch=(2000)
star._ra ='2:31:47'
star._dec = '89:15:50'
star.compute(telescope)
print(ephem.constellation(2,2))
