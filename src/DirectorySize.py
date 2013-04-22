#!/usr/local/bin/python2.6

# determine size of a given folder in MBytes
import os
# pick a folder you have ...

def getDirectorySize(directory):
    folder = directory
    folderSize = 0
    filesOverTenMb = []
    fileLimit = 10485760
   
    for (path, dirs, files) in os.walk(folder):
        for file in files:
            filename = os.path.join(path, file)
	    try:
     	        filesOverTenMb.append(filename) if os.path.getsize(filename) > fileLimit else 'false'
	    	folderSize += os.path.getsize(filename)
	    except OSError as ose:
		print 'An OS error occured :%s' %ose
    #print filesOverTenMb
    return (folderSize/(1024*1024.0),filesOverTenMb)

def main():
    print('/var/log = %i MB \n %s' % getDirectorySize('/var/log'))

if __name__ == "__main__":
    main()
