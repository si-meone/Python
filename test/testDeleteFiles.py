import unittest
import deleteFiles
from System.IO import Directory, File, FileStream, FileMode
from System import Environment as Env

class Test(unittest.TestCase):

    temp_directory = Env.GetEnvironmentVariable("TEMP")
    temp_file1 = r"\test1.test"
    temp_file2 = r"\test2.test"
    temp_file3 = r"\test3.test"
    tempFileFullPath1 = temp_directory + temp_file1
    tempFileFullPath2 = temp_directory + temp_file2
    tempFileFullPath3 = temp_directory + temp_file3

    def setUp(self):
        self.temp_directory = Env.GetEnvironmentVariable("TEMP")
        #check temp dir exists
        self.assertTrue(Directory.Exists(self.temp_directory))
        #check temp file in temp dir does not exist
        if File.Exists(self.tempFileFullPath1 or self.tempFileFullPath2 or self.tempFileFullPath1):
            File.Delete(self.tempFileFullPath1)
            File.Delete(self.tempFileFullPath2)
            File.Delete(self.tempFileFullPath3)
        #create a file to check and delete
        fs1 = FileStream(self.tempFileFullPath1, FileMode.Create)
        fs2 = FileStream(self.tempFileFullPath2, FileMode.Create)
        fs3 = FileStream(self.tempFileFullPath3, FileMode.Create)
        fs1.Close();
        fs2.Close();
        fs3.Close();
        
    def tearDown(self):
        self.assertFalse(File.Exists(self.tempFileFullPath1))
        self.assertFalse(File.Exists(self.tempFileFullPath2))
        self.assertFalse(File.Exists(self.tempFileFullPath3))

    def testDeleteAFile(self):
#        File.Delete(self.tempFileFullPath1)
        deleteFiles.deleteFilesFromDirectoryWithExtension(self.temp_directory, "test")
        self.assertFalse(File.Exists(self.tempFileFullPath1))
        self.assertFalse(File.Exists(self.tempFileFullPath2))
        self.assertFalse(File.Exists(self.tempFileFullPath3))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()