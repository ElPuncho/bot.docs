#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import py_files.filesystemhandler as fsh
import py_files.crawler as cwl
import py_files.collaborativeFiltering as cfl

class ControlManager:
    def __init__(self, query):
        self.query = query
        self.filterObject = None
        self.crawlerObject = None
        self.fileHandler = fsh.FileSystemHandler()
    
    def initSession(self):
        self.fileHandler.createRootDirectory()
        
    def closeSession(self):
        self.fileHandler.deleteSessionTempFiles(self.fileHandler.getRootDirectory())
        
    def crawlQuery(self):
        self.crawlerObject = cwl.Crawler(self.query)
        self.crawlerObject.writeTextToFile(self.crawlerObject.getTextFromWebsite(self.crawlerObject.getLibUrl()))
        
    def executeFiltering(self):
        self.filterObject = cfl.CollaborativeFiltering(self.fileHandler.getRootDirectory() + self.fileHandler.getSlashForOsVersion(), self.query.split(":")[2])
        return self.filterObject.generateResponse()
        
if __name__ == "__main__":
    con = ControlManager("c++:vector:create vector")
    con.initSession()
    con.crawlQuery()
    print(con.executeFiltering())
    con.closeSession()