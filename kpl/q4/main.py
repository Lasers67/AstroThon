import ephem
from datetime import datetime
from datetime import time

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
	saturn = ephem.Saturn()
	saturn.compute(obstime)
	body = ephem.FixedBody()
	body._ra = saturn.ra
	body._dec = saturn.dec
	Gravity = ephem.Observer()
	Gravity.lat = '31.7754'
	Gravity.lon = '76.9861'
	Gravity.date = obstime
	body.compute(Gravity)
	return((body.az, body.alt))

print(findSaturn(startobs))