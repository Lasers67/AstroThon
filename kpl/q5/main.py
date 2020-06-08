# all imports below
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.request import urlopen
from bs4 import BeautifulSoup

"""
Any extra lines of code (if required)
as helper for this function.
"""
url = "http://solar.physics.montana.edu/HINODE/XRT/QL/syn_comp_fits/"
html = urlopen(url)

soup = BeautifulSoup(html, 'lxml')
title = soup.title
print(title)

all_links = soup.find_all("a")
print(len(all_links))


class ScraperXRT:
	'''
	Description
	-----------
	A class to scrap XRT files from the telescope archive.
	'''

	def __init__(self, typeof_file, startime, endtime):
		'''
	    Parameters
		----------
		typeof_file: A `string`
	    startime: A `~datetime.datetime` instance
	    endtime: A `~datetime.datetime` instance
		'''
	def query(self):
		'''
		Returns
		-------
		A `list` of strings of URLs.
		'''
		a = []
		for link in all_links:
			x = link.split("_")
			filetype = x[1]+x[2]
			time = datetime(x[3][0:4],x[3][4:6],x[3][6:8],x[4][0:2],x[4][2:4],x[4][4:6])
			if(time>=startime and time<=endtime):
				a.append(x)

		return a

	def get(self):
		'''
		Returns
		-------
		A `list` of strings for files.
		'''
		return NotImplementedError

	def view(self, filepath):
		'''
	    Parameters
		----------
	    filepath: A `string` representing absolute path of file in system.

		Returns
		-------
		An instance of `matplotlib.image.AxesImage`, returned using `plt.imshow(data)`.
		'''
		return NotImplementedError
