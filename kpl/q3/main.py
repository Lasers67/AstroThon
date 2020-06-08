# all imports below
#%%
"""
As helper for this function.
This Function takes the radius of satellite's orbit from the centre of the earth in metre
Then using it, it calculates the time delay of the Earth-Satellite System in nanoseconds.
"""

def findDelay(dist):
	'''
	Parameters
	----------
	dist : A `float` - The radius of satellite orbit in metres
	
	Returns
	-------
	A `float` - Time nanoseconds gained by the satellite w.r.t Earth due to relativistic time dilation
	'''

	R = 6357000
	M = 5974000000000000000000000
	c = 299800000
	G = 0.00000000006674

	if(dist<R):
		return 'The radius of satellite orbit can not be smaller than Radius of Earth(6357000) '

	# First calculate the velocity of satellite
	v = (G*M/dist)**(0.5) 
	# print(v)

	# Then for calculation calculate the factor
	timelapseconstant = (1 - (v*v)/(c*c))**(0.5)
	# print("timelapseconstant",timelapseconstant)

	# Find the time period to reach the light to satellite
	T = (dist - R)/c # check this if this can be find by another method of more accuracy

	# Calculating time on satellite
	timeOnSatelite = T / timelapseconstant
	# print(T)
	# print(timeOnSatelite)

	return((timeOnSatelite - T)*1000000000)



# Sample 
# print(findDelay(2*6357000))
if __name__ == '__main__':
	print(findDelay(eval(input("Enter radius of satellite: "))))

