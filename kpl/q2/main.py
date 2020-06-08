# all imports below

"""
Any extra lines of code (if required)
as helper for this function.
"""

def findDistance(vrec):
	'''
	Parameters
	----------
	vrec : a `float`
	
	Returns
	-------
	a `float`
	'''

	distanceinmpc = vrec/71

	#1 Mpc=3.2 x 106 light-years

	distanceinly = distanceinmpc*3.2*1000000

	return distanceinly

# print(findDistance(68300))