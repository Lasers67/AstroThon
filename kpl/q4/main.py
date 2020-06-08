import ephem
from datetime import datetime
from datetime import time
from datetime import timedelta
import math 
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
import numpy as np
import matplotlib.pyplot as plt

"""
Any extra lines of code (if required)
as helper for this function.
"""

startobs = datetime(2000, 1, 1, 0, 0, 0) #replace it by the time when Saturn will be just visible
endobs = datetime(2020, 1, 1) #replace it by the time when Saturn is no longer visible from SAC terrace

def findSaturn(obstime):
	'''
	Parameters
	----------
	obstime : A `~datetime.datetime` instance.
	
	Returns
	-------
	A `tuple` of two floats.
	'''


	m33 = SkyCoord.from_name('M33')
	bear_mountain = EarthLocation(lat=31.7754*u.deg, lon=-76.9861*u.deg, height=1000*u.m)
	utcoffset = -4*u.hour  # Eastern Daylight Time
	time = Time('2012-7-12 23:00:00') - utcoffset

	m33altaz = m33.transform_to(AltAz(obstime=time,location=bear_mountain))
	# print("M33's Altitude = {0.alt:.2}".format(m33altaz))

	print(m33altaz.alt, m33altaz.az)

	# saturn = ephem.Saturn()
	# saturn.compute(obstime)
	# body = ephem.FixedBody()
	# body._ra = saturn.ra
	# body._dec = saturn.dec
	# Gravity = ephem.Observer()
	# Gravity.lat = '31.7754'
	# Gravity.lon = '76.9861'
	# Gravity.date = obstime
	# body.compute(Gravity)

	# return((body.alt, body.az))

# print(findSaturn(startobs))
# current = startobs
# i=0
# while(current<endobs):
# 	altitude = math.degrees(findSaturn(current)[0])
# 	if(altitude>=-20):
# 		startobs = current
# 	current = current + timedelta(hours=1)
# 	i+=1

# current = startobs
# i=0
# while(current<endobs):
# 	altitude = math.degrees(findSaturn(current)[0])
# 	if(altitude>=-160):
# 		endobs = current
# 	current = current + timedelta(hours=1)
# 	i+=1


print(startobs)
print(findSaturn(startobs))
# print(math.degrees(findSaturn(startobs)[0]))

# print(endobs)
# print(findSaturn(endobs))
# print(math.degrees(findSaturn(endobs)[0]))