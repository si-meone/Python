#!/usr/local/bin/python2.6

# determine size of a given folder in MBytes
import os
# pick a folder you have ...

def truncateFile(fullpath):
    file = open(fullpath, 'rw+')
    file.truncate(0)
    
def main():
    fullpath = '/var/log/messages'
    print('%s file size before truncateLog is %0.1f' % (fullpath, os.path.getsize(fullpath)/(1024*1024.0)))		
    print('truncating %s ...' % fullpath)
    truncateLog(fullpath)
    print('%s file size after truncateLog is %0.1f' % (fullpath,os.path.getsize(fullpath)/(1024*1024.0)))		

if __name__ == "__main__":
    main()
