import subprocess
import glob
import re
import os

fs = glob.glob("A*.hdf")
print len(fs)
for f in fs:
	outfile = f[:-4]+'_3310'
	#if outfile + "_sur_refl_b01.tif" not in os.listdir(os.getcwd()) or \
	#	outfile + "_sur_refl_b02.tif" not in os.listdir(os.getcwd()):
	com = 'modis_convert.py -s "( 1 1 1 1 )" -o ' + outfile + ' -e 3310 '+ f
	print com 
	subprocess.Popen('modis_convert.py -s "( 1 1 0 0 )" -o ' + outfile + ' -e 3310 -g 250 '+ f, shell=True).wait()

#clip modis image using state polygone
inshp =  '../shp/cnty24k09_1_state_poly.shp'

tifs = glob.glob('A*3310*.tif' )
for t in tifs:
	print t
	clipCom1 = ' '.join(['gdalwarp',\
	'-s_srs "+proj=aea +lat_1=34 +lat_2=40.5 +lat_0=0 +lon_0=-120 +x_0=0 +y_0=-4000000 +datum=NAD83 +units=m +no_defs "',\
	'-cutline', inshp, '-crop_to_cutline', t,re.search('A\d+',t).group(0) + t[23:26] +'_ca.tif'])
	print clipCom1
     	subprocess.Popen(clipCom1, shell=True).wait()
                                                             
