import os 
import re
import glob
import subprocess
from Queue import Queue
os.chdir(os.getcwd())

infileNamesList = glob.glob('M*hdf')
infileNames = sorted(infileNamesList, key = lambda x: re.search('A\d+\.h\d+v\d+', x))


def newParaFile(infileName, outfileName):
	with open('/home/wryang/etdata/mrtPara.txt', 'r') as f:
		with open('/home/wryang/etdata/mrtPara2.prm', 'w') as fo:
			lines = f.readlines()
			print lines[1]
			lines[1] = 'INPUT_FILENAME = ' + infileName+'\r\n'
			lines[10] = 'OUTPUT_FILENAME = ' + outfileName+'\r\n'
			fo.writelines(lines)
			fo.flush()
	#os.rename('/home/wryang/etdata/mrtPara2.txt', '/home/wryang/etdata/mrtPara2.prm')

def aggFiles(inf1,inf2,inf3):
	with open('para'+ re.search('A\d+',inf1).group(0) + '.prm', 'w') as fo:
		fo.write(inf2+'\r\n')
		fo.write(inf1+'\r\n')
		fo.write(inf3+'\r\n')
	#~/MRT/bin/mrtmosa2ic -i mosaicPara.prm -s "1 1 1 1" -o mo.hdf
	print('/home/wryang/MRT/bin/mrtmosaic -i '+ 'para'+ re.search('A\d+',inf1).group(0) + '.prm -s "1 1 1 1" -o ' + re.search('A\d+',inf1).group(0) + '.tif')
	subprocess.Popen('/home/wryang/MRT/bin/mrtmosaic -i '+ 'para'+ re.search('A\d+',inf1).group(0) + '.prm -s "1 1 1 1" -o ' + re.search('A\d+',inf1).group(0) + '.hdf', shell=True).wait()



fs = glob.glob('M*hdf')
fs2 = sorted(fs, key=lambda x: re.search('A\d+\.h\d+v\d+',x).group(0))

for infileName in infileNames:
	pass
	#print infileName
	#outfileName = '/home/wryang/etdata/modisTemp/'+re.search('A\d+.h\d+v\d+',infileName).group(0)+'.tif'
	#print outfileName
	#newParaFile(infileName, outfileName)
	#subprocess.Popen('/home/wryang/MRT/bin/resample -p mrtPara2.prm', shell=True).wait()

for i in range(2005,2016):
	files=glob.glob('/home/wryang/etdata/modisTemp/M*A'+str(i)+'*hdf')
	if len(files) != 138:
		print "year %d %d" %(i, len(files))
	else:
		print "year %d" %i
	



f1 = []
f2 = []
f3 = []
for f in fs2:
	if 'h08v04' in f:
		f1.append(f)
	if 'h08v05' in f:
		f2.append(f)
	if 'h09v04' in f:
		f3.append(f)

print len(f1)
print len(f2)
print len(f3)
for i in range(len(f1)):
	print f1[i],f2[i],f3[i]
	aggFiles(f1[i],f2[i],f3[i])
	
