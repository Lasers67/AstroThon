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
import matplotlib.pyplot

import numpy as np
import urllib.request

"""
Any extra lines of code (if required)
as helper for this function.
"""
url = "http://solar.physics.montana.edu/HINODE/XRT/QL/syn_comp_fits/"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
all_links = soup.find_all("a")
for i in range(len(all_links)):
	#print (link['href'])
	all_links[i]=all_links[i]['href']
all_links=all_links[5::]
class ScraperXRT:
    
    global link_array
    global path_array
    link_array=[]
    path_array=[]
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
		        link_array.append(link)

    def query(self):
	    return link_array

    def get(self):
        print("beginning download")
        for link in link_array:
            url="http://solar.physics.montana.edu/HINODE/XRT/QL/syn_comp_fits/" + link
            urllib.request.urlretrieve(url, link)
            l="./"+link
            path_array.append(l)

        return path_array

    def view(self, filepath):

    	hdul=fits.open(filepath)
    	data=hdul[0].data
    	
    	img=matplotlib.pyplot.imshow(data)
    	
    	return img



x=ScraperXRT('Al_mesh',datetime(2015,1,1),datetime(2015,1,2))
