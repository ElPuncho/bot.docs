#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest, os
import py_files.crawler as cw
from bs4 import BeautifulSoup 

class TestClient(unittest.TestCase):
    def testInit(self):
        query = "python:math:how to use sine"
        c = cw.Crawler(query)
        self.assertEqual(c.query, query)
        
    def testGetLibUrl(self):
        query, libUrl = "python:math:how to use sine", "https://docs.python.org/3/library/math.html"
        c = cw.Crawler(query)
        self.assertIs(type(c.getLibUrl()), type(libUrl))
        self.assertEqual(c.getLibUrl(), libUrl)
    
    def testGetTextFromWebsite(self):
        query = "python:math:how to use sine"
        c = cw.Crawler(query)
        htmlCode = c.getTextFromWebsite(c.getLibUrl())
        self.assertIs(type(htmlCode), BeautifulSoup)
        
    def testWriteTextToFile(self):
        query = "python:math:how to use sine"
        c = cw.Crawler(query)
        c.writeTextToFile(c.getTextFromWebsite(c.getLibUrl()))
        self.assertTrue(os.path.isfile(c.handler.getSearchFilePath("python", "math.txt")))
        file = open(c.handler.getSearchFilePath("python", "math.txt")).read()
        self.assertTrue("sin" in file and "cos" in file and "<html>" not in file)

if __name__ == "__main__":
    unittest.main()
