# all imports below
from astropy.io import fits
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
from datetime import datetime
"""
Any extra lines of code (if required)
as helper for this function.
"""
url = "http://solar.physics.montana.edu/HINODE/XRT/QL/syn_comp_fits/"
#html = urlopen(url)
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
#soup = BeautifulSoup(html, 'html.parser')
title = soup.title
print(title)
all_links = soup.find_all("a")
for i in range(len(all_links)):
	#print (link['href'])
	all_links[i]=all_links[i]['href']
all_links=all_links[5::]
#print(all_links[0:2])
from PIL import Image
import numpy as np

w, h = 512, 512

"""
Any extra lines of code (if required)
as helper for this function.
"""
p=1;
import urllib.request

print('Beginning file download with urllib2...')


class ScraperXRT:
    '''
    Description
    -----------
    A class to scrap XRT files from the telescope archive.
    '''
    global a
    global b
    a=[]
    b=[]
    def __init__(self, typeof_file, startime, endtime):
	    for link in all_links:
		    x = link.split("_")
		    #print(x)
		    filetype=x[1]+"_"+x[2]
		    t=x[-2]
		    tt=x[-1]
		    y=int(t[0:4])
		    m=int(t[4:6])
		    d=int(t[6:8])

		    #print(m)
		    time=datetime(y,m,d)
		    #print(time)
		    if(filetype==typeof_file and time>=startime and time<=endtime):
		        a.append(link)

    def query(self):
	    return a

    def get(self):
	    for link in a:
	    	url="http://solar.physics.montana.edu/HINODE/XRT/QL/syn_comp_fits/" + link
	    	urllib.request.urlretrieve(url, link)
	    	l="./"+link
	    	b.append(l)

	    return b

    def view(self, filepath):
	    '''
	    Parameters
		----------
	    filepath: A `string` representing absolute path of file in system.

		Returns
		-------
		An instance of `matplotlib.image.AxesImage`, returned using `plt.imshow(data)`.
		'''
		hdul = fits.open(filepath)
		data=hdul[0].data
        img = Image.fromarray(data, 'RGB')
        img.show()

	    return img

#data = np.zeros((h, w, 3), dtype=np.uint8)
#data[0:256, 0:256] = [255, 0, 0] # red patch in upper left

hdul = fits.open('XRT_Al_mesh_20140110_181442.9.fits')
#hdul = fits.open(fits_image_filename)
data=hdul[0].data
#print(hdul[0].data[30:40, 10:20])
img = Image.fromarray(data, 'RGB')
#img.save('my.png')
#img.show()
x=ScraperXRT('Al_mesh',datetime(2015,1,1),datetime(2015,1,3))
print(x.get())