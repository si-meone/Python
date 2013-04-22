#!/usr/local/bin/python2.6

import syslog

from FreeSpace import freespace
from DirectorySize import getDirectorySize  
from Mailer import mail
from Truncater import truncateFile

# disksize
limitInBytes = 1024000
dirToCheck ='/'
logDir = '/var/log'

freespaceInBytes = freespace(dirToCheck)
(logDirectorySize, filesOverTenMb) = getDirectorySize(logDir)

if freespaceInBytes < limitInBytes :
    print ('Hit Limit of free space %s:' %freespaceInBytes)
    syslog.syslog('Disk is running low on space = %i MB' % (freespaceInBytes/1024))
    print ('emailing...%s' % mail(
        'simon_nasrallah@hotmail.com ',
        'Diskspace hit limit of %i MB' % (limitInBytes/1024),
        'You have %i Mb left \n log directory is %i Mb' % ((freespaceInBytes/1024), logDirectorySize)
	))
    print ('Running some log clearing... %s' % filesOverTenMb)
    syslog.syslog('Running some log clearing... %s' % filesOverTenMb)
    for file in filesOverTenMb:
        truncateFile(file)
    print ('Space After Log clearing is %s:' %freespaceInBytes)
    syslog.syslog('After log clear disk space is now %i MB' % (freespaceInBytes/1024))
    print ('emailing...%s' % mail(
        'simon_nasrallah@hotmail.com ',
        'After log clear diskspace',
        'You have %i Mb left \n log directory is %i Mb' % ((freespaceInBytes/1024), logDirectorySize)
        ))
else:
    print ('Disk has enough free space = %i MB' % (freespaceInBytes/1024)) 
    syslog.syslog('Disk has enough free space = %i MB' % (freespaceInBytes/1024))
