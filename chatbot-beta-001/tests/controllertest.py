#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest, os
import py_files.filesystemhandler as fsh
import py_files.controller as cont

class TestController(unittest.TestCase):
    def testInit(self):
        query = "python:math:how to use sine"
        con = cont.ControlManager(query)
        self.assertEqual(con.query, query)
        self.assertEqual(con.filterObject, None)
        self.assertEqual(con.crawlerObject, None)
        self.assertIs(type(con.fileHandler), fsh.FileSystemHandler)
        
    def testInitSession(self):
        query = "python:math:how to use sine"
        con = cont.ControlManager(query)
        con.initSession()
        self.assertTrue(os.path.isdir(con.fileHandler.getRootDirectory()))
        
    def testCrawlQuery(self):
        query = "python:math:how to use sine"
        con = cont.ControlManager(query)
        con.initSession()
        con.crawlQuery()
        self.assertTrue(con.fileHandler.getSearchFilePath("python", "math.txt"))
        fileTest = open(con.fileHandler.getSearchFilePath("python", "math.txt")).read()
        self.assertTrue("sin" in fileTest and "cos" in fileTest and "<html>" not in fileTest)
    
    def testExecuteFiltering(self):
        query = "python:math:how to use sine"
        con = cont.ControlManager(query)
        con.initSession()
        con.crawlQuery()
        result = con.executeFiltering()
        self.assertTrue("sin(x)" in result)
        
    def testCloseSession(self):
        query = "python:math:how to use sine"
        con = cont.ControlManager(query)
        con.initSession()
        con.crawlQuery()
        result = con.executeFiltering()
        con.closeSession()
        rootDir = con.fileHandler.getRootDirectory()
        self.assertTrue(os.path.exists(rootDir) and os.path.isdir(rootDir) and not os.listdir(rootDir))
        

if __name__ == "__main__":
    unittest.main()

