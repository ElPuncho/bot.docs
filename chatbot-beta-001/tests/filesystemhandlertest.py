#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest, os
import py_files.filesystemhandler as fsh

class TestClient(unittest.TestCase):
    def testInit(self):
        f = fsh.FileSystemHandler()
        self.assertTrue(os.path.isdir(f.getRootDirectory()))
    
    def testGetRootDirectory(self):
        rootDir = "/home/philipp/Dokumente/5. Semester/Softwarepraktikum_Chatbot/chatbot-alpha/chatbot-alpha-001/tests/data"
        f = fsh.FileSystemHandler()
        self.assertEqual(f.getRootDirectory(), rootDir)
        
    def testGetSlashForOsVersion(self):
        f = fsh.FileSystemHandler()
        self.assertEqual(f.getSlashForOsVersion(), "/")
    
    def testCheckDirElseMkDir(self):
        f = fsh.FileSystemHandler()
        testFolder = f.getRootDirectory() +  f.getSlashForOsVersion() + "testIfMkDir"
        f.checkDirElseMkDir(testFolder)
        self.assertTrue(os.path.isdir(testFolder))
        
    def testGetSearchFilePath(self):
         f = fsh.FileSystemHandler()
         subdir, filename = "c++", "vector.txt"
         filePath = f.getRootDirectory() + f.getSlashForOsVersion() + subdir + f.getSlashForOsVersion() + filename
         self.assertEqual(f.getSearchFilePath(subdir, filename), filePath)
        
    def testDeleteSessionTempFiles(self):
        f = fsh.FileSystemHandler()
        dataDir = f.getRootDirectory()
        f.deleteSessionTempFiles(dataDir)
        self.assertFalse(os.path.isdir(dataDir + f.getSlashForOsVersion() + "testIfMkDir"))
        
if __name__ == "__main__":
    unittest.main()

