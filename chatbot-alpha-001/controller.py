#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import py_files.filesystemhandler as fsh
import py_files.crawler as cwl

class ControlManager:
    def __init__(self):
        self.crawlerObject = None
        self.fileHandler = fsh.FileSystemHandler()
    
    def initSession(self):
        self.fileHandler.createRootDirectory()
        
    def closeSession(self):
        self.fileHandler.deleteSessionTempFiles(self.fileHandler.getRootDirectory())
        
    def crawlQuery(self, query):
        self.crawlerObject = cwl.Crawler(query)
        self.crawlerObject.writeTextToFile(self.crawlerObject.getTextFromWebsite(self.crawlerObject.getLibUrl()))
        
if __name__ == "__main__":
    con = ControlManager()
    con.initSession()
    con.crawlQuery("python:math:sin")
    #con.closeSession()