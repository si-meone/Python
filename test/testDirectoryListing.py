import unittest
import DirectoryListing
from System.IO import DirectoryInfo


class TestDirectoryListing(unittest.TestCase):
        
    dir_to_check = r"C:\Documents and Settings\default\My Documents"

    def testDirectoryExists(self):
        self.assertTrue(DirectoryListing.exists(self.dir_to_check))
    
    def testDirectoryListing(self):
        files, dirs = DirectoryListing.getFilesAndDirs(self.dir_to_check)
        self.assertTrue(10, files.Count > 1) 
        self.assertTrue(1, dirs.Count > 1)
    
    def testDirectorySize(self):
        self.assertEqual(30, DirectoryListing.getDirSize(DirectoryInfo(self.dir_to_check)))
          
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()