import unittest
import sys
sys.path.append("z:\\python\\FileUtils\src") 
from System.IO import DirectoryInfo, Directory, FileInfo, FileStream, FileMode, StreamWriter
from System import Environment 
from System import DateTime, ArgumentNullException

import directoryListing
import deleteFiles

class TestDirectoryListing(unittest.TestCase):

    def setUp(self):
        temp_dir = DirectoryInfo(Environment.GetEnvironmentVariable("TEMP"))
#       myDocuments = DirectoryInfo(Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments))
        self.temp_dir = temp_dir.CreateSubdirectory('tempDir')
        self.temp_dir_path = self.temp_dir.ToString()
        
        self.file1 = FileInfo(self.temp_dir_path + '\\file1.txt')
        self.file2 = FileInfo(self.temp_dir_path + '\\file2.txt')
        self.file3 = FileInfo(self.temp_dir_path + '\\file3.txt')

        sw = self.file1.CreateText()
        sw.WriteLine("Hello1")
        sw.Close()
        
        sw = self.file2.CreateText()
        sw.WriteLine("Hello2")
        sw.Close()

        sw = self.file3.CreateText()
        sw.WriteLine("Hello3")
        sw.Close()

        today = DateTime.Now
        one_day_old = today.AddDays(-1).ToString("yyyy.MM.dd")
        two_days_old = today.AddDays(-2).ToString("yyyy.MM.dd")
        self.file1.CreationTime = DateTime.Parse(today.ToString("yyyy.MM.dd"))
        self.file2.CreationTime = DateTime.Parse(one_day_old)
        self.file3.CreationTime = DateTime.Parse(two_days_old)
        
        print "\r myDocuments temp path = [%s]" % self.temp_dir_path
        print "CreationTime file1 = [%s]" % self.file1.CreationTime
        print "CreationTime file2 = [%s]" % self.file2.CreationTime
        print "CreationTime file3 = [%s]" % self.file3.CreationTime
    
    def testFindThreeFilesInDirectory(self):
        files = directoryListing.getFilesOlderThan(self.temp_dir_path)
        self.assertEqual("file1.txt", files[0].Name)
        self.assertEqual("file2.txt", files[1].Name)
        self.assertEqual("file3.txt", files[2].Name)
    

    def testFindFilesInDirectoryADayOrOlderFromNow(self):
        files = directoryListing.getFilesOlderThan(self.temp_dir_path,1)
        self.assertEqual("file2.txt", files[0].Name)
        self.assertEqual("file3.txt", files[1].Name)
    
    def testFindFilesInDirectoryTwoDaysOrOlderFromNow(self):
        files = directoryListing.getFilesOlderThan(self.temp_dir_path,2)
        self.assertEqual("file3.txt", files[0].Name)
 
    def testDeleteAllFilesInDirectory(self):
        files = directoryListing.getFilesOlderThan(self.temp_dir_path)
        deleteFiles.deleteFiles(files)
        self.assertEqual(0, len(Directory.GetFileSystemEntries(self.temp_dir_path)))

    def testDeleteFilesInDirectoryOneDayAndOlder(self):
        all_files = directoryListing.getFilesYoungerThan(self.temp_dir_path)
        files = directoryListing.getFilesYoungerThan(self.temp_dir_path,1)
        deleteFiles.deleteFiles(files)
        self.assertEqual(1, len(Directory.GetFileSystemEntries(self.temp_dir_path)))

    def testDeleteFilesInDirectoryTwoDaysAndYounger(self):
        all_files = directoryListing.getFilesYoungerThan(self.temp_dir_path)
        files = directoryListing.getFilesYoungerThan(self.temp_dir_path,2)
        deleteFiles.deleteFiles(files)
        self.assertEqual(0, len(Directory.GetFileSystemEntries(self.temp_dir_path)))

    def tearDown(self):
        self.temp_dir.Delete(True)
                  
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
