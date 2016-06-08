#!/usr/bin/env python

"""File downloading from the web.
"""

import os
import urllib2
import re
from datetime import date, timedelta
import wget


def download(url):
	"""Copy the contents of a file from a given URL
	to a local file.
	"""
	
	wf = urllib2.urlopen(url)
	html=wf.read()
	# print html
	flist=[]

	mhdf = re.findall('\"M.*\.hdf\"', html)
	mhdfs =[f for f in mhdf if 'h08v04' in f or 'h08v05' in f or 'h09v04' in f]
	# print mhdfs
	for line in mhdfs:
		# print 'a line', line.replace('\"', '')
		fileUrl=url+line.replace('\"', '')
		print fileUrl
		wget.download(fileUrl)

	xhdf = re.findall('\"M.*\.hdf.xml\"', html)
	xhdfs =[f for f in xhdf if 'h08v04' in f or 'h08v05' in f or 'h09v04' in f]
	for line in xhdfs:
		# print 'a line', line.replace('\"', '')
		xfileUrl=url+line.replace('\"', '')
		print xfileUrl
		wget.download(xfileUrl)


if __name__ == '__main__':
	for year in range(2008, 2016):
		d0=date(year, 1, 1)
		for i in range(0, 365, 8):
			d = d0+timedelta(days=i)
			# print d
			# print str(d).replace('-', '.')
			url='http://e4ftl01.cr.usgs.gov/MOLT/MOD09Q1.006/'
			# print url+str(d).replace('-', '.')+'/'
			download(url+str(d).replace('-', '.')+'/')

			# check if any ts point missiing file
			#a=(2006*h09v04*hdf);echo ${#a[@]}
			# for f in ${a[@]}; do echo $f; done
			# for f in ${a[@]}; do mv $f ${f:3:20}.tif; done
			
			# this file is missing from the html but can be download 
			# MYD09Q1.A2009097.h09v04.006.2015188124448.hdf
			# 2010.07.04MOD09Q1.A2010185.h08v04.006.2015208230553.hdf

