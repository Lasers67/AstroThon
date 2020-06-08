# all imports below
import math
import nvector as nv
"""
Any extra lines of code (if required)
as helper for this function.
"""

def findstrike(v, alt, az):
	alt=math.radians(alt)
	G=6.673*(10**-11)
	M=5.97219*(10**24)
        Re=6371000.0
	Ri=2*Re*G*M/(2*G*M-((v*math.sin(alt))**2)*Re)
	t=((2*(Re**3)/(G*M))**0.5)*(math.atan((Re/(Ri-Re))**0.5)-((Re*(Ri-Re))/Ri)**0.5+math.pi/2)
	d= v*math.cos(alt)*t

	frame = nv.FrameE(a=6371e3, f=0)
	pointA = frame.GeoPoint(latitude=27.9881, longitude=86.9250, degrees=True)
	pointB, _azimuthb = pointA.displace(distance=d, azimuth=az,degrees=True)
	lat, lon = pointB.latitude_deg, pointB.longitude_deg

	return (lat,lon)
