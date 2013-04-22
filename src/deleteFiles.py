from System.IO import Directory, File



def deleteFilesFromDirectoryWithExtension(dir, file_extension):
    files = Directory.GetFileSystemEntries(dir)
    for file in files:
        if file.EndsWith(file_extension):
            print "deleting %s" % file 
            File.Delete(file)

def deleteFiles(files):
    for file in files:
        print "deleting %s" % file 
        file.Delete()

if __name__ == "__main__":
    dir = r"d:\ImageStudio\Album\Motion Images"
    file_extension = "avi"
    deleteFilesFromDirectoryWithExtension(dir, file_extension)
