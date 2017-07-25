import os, glob, time, zipfile
from stat import *
from datetime import date,datetime, timedelta

sourcefolder="/opt/dump/"
fileListToZip=[]
zipFilename="/opt/myzipfile.zip"

yesterday = date.today() - timedelta(1)


def createZip():
	zf = zipfile.ZipFile(zipFilename, "w",zipfile.ZIP_DEFLATED)
	for files in fileListToZip:
		print "Add ["+str(files)+"] in zip."
		zf.write(os.path.join(files))
	zf.close()


def checkFile(filename):
	#(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(filename)
	(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(filename)
	C_Time = datetime.strptime(datetime.fromtimestamp(ctime).strftime('%Y-%m-%d %H:%M:%S'), "%Y-%m-%d %H:%M:%S")
	M_Time = datetime.strptime(datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S'), "%Y-%m-%d %H:%M:%S")
	A_Time = datetime.strptime(datetime.fromtimestamp(atime).strftime('%Y-%m-%d %H:%M:%S'), "%Y-%m-%d %H:%M:%S")
	
	if C_Time.date()== yesterday or M_Time.date()== yesterday or A_Time.date()== yesterday:
		#print filename
		#print("-----------------[C_Time: "+str(C_Time.date())+"][M_Time: "+ str(M_Time.date())+"][A_Time: "+str(A_Time.date())+"]")
		return True
	else:
		return False


def getFiles(top):
	'''recursively descend the directory tree rooted at top,
	calling the callback function for each regular file'''

	for f in os.listdir(top):
		pathname = os.path.join(top, f)
		mode = os.stat(pathname)[ST_MODE]
		if S_ISDIR(mode):
			getFiles(pathname)
		elif S_ISREG(mode):			
			if(checkFile(pathname)):
				fileListToZip.append(pathname)			
		else:
			print 'Skipping %s' % pathname


getFiles(sourcefolder)
createZip()
strCammand=""


By Chaitali************************
By Pranali-----------------------------------

