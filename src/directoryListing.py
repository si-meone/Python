from System.IO import Directory, FileInfo
from sys import stderr
from System import DateTime

def exists(dir):
    if Directory.Exists(dir):
        return True
    return False

def getFilesOlderThan(dir, older_than=0):
    if exists(dir):
        files = Directory.GetFiles(dir)
        date_to_check = DateTime.Parse(DateTime.Now.AddDays(-older_than).ToString("yyyy.MM.dd"))
        files_of_age = [] 
        for file in files:
            file = FileInfo(file)
            print file
            result = DateTime.Compare(file.CreationTime, date_to_check);

            if result < 0:
                relationship = "is earlier than %s" %date_to_check
                files_of_age.append(file)
            elif result == 0:
                relationship = "is the same time as %s" %date_to_check         
                files_of_age.append(file)
            else:
                relationship = "is later than %s" %date_to_check
            print relationship
        return files_of_age

def getFilesYoungerThan(dir, younger_than=0):
    if exists(dir):
        files = Directory.GetFiles(dir)
        date_to_check = DateTime.Parse(DateTime.Now.AddDays(-younger_than).ToString("yyyy.MM.dd"))
        files_of_age = [] 
        for file in files:
            file = FileInfo(file)
            print file
            result = DateTime.Compare(file.CreationTime, date_to_check);

            if result < 0:
                relationship = "is earlier than %s" %date_to_check
            elif result == 0:
                relationship = "is the same time as %s" %date_to_check
                files_of_age.append(file)         
            else:
                relationship = "is later than %s" %date_to_check
                files_of_age.append(file)
            print relationship
        return files_of_age

            

def getDirSize(dirinfo):
    size = 0
    try:
        for afile in dirinfo.GetFiles():
            size += afile.Length
        for adir in dirinfo.GetDirectories():
            size += getDirSize(adir)
    except Exception, details:
        print >> stderr, "Warning [%(details)s]" % {'details' : details}
    return size  

if __name__ == '__main__':
    pass