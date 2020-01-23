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
        rootD = self.fileHandler.getRootDirectory()
        self.fileHandler.deleteSessionTempFiles(rootD)

    def crawlQuery(self):
        self.crawlerObject = cwl.Crawler(self.query)
        lib = self.crawlerObject.getLibUrl()
        text = self.crawlerObject.getTextFromWebsite(lib)
        self.crawlerObject.writeTextToFile(text)

    def executeFiltering(self):
        file = self.fileHandler.getRootDirectory()
        file += self.fileHandler.getSlashForOsVersion()
        searchString = self.query.split(":")[2]
        self.filterObject = cfl.CollaborativeFiltering(file, searchString)
        return self.filterObject.generateResponse()


if __name__ == "__main__":
    con = ControlManager("c++:vector:create vector")
    con.initSession()
    con.crawlQuery()
    print(con.executeFiltering())
    con.closeSession()
