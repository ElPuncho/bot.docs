#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import py_files.filesystemhandler as fsh
import py_files.crawler as cwl
import py_files.preprocessor as pre
import py_files.pearson as pear
import py_files.kmeans as kmeans

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
        file = self.fileHandler.getSearchFilePath(self.query.split(":")[0],
                                                  self.query.split(":")[1] +
                                                  ".txt")
        searchString = self.query.split(":")[2]
        self.filterObject = pre.Preprocessor(file, searchString)
        matrix = self.filterObject.vectoriseData()
        text = self.filterObject.removeDuplicateLines()
        
        t = pear.Pearson(matrix, text)
        with open(self.fileHandler.getSearchFilePath(self.query.split(":")[0],"preprocessed.txt"), "w", encoding="utf8") as f:
            f.write('\n'.join([x for x in t.generateResponse().split('\n') if len(x) <= 1000]))
        
        self.filterObject = pre.Preprocessor(self.fileHandler.getSearchFilePath(self.query.split(":")[0],"preprocessed.txt"), searchString)
        matrix = self.filterObject.vectoriseData()
        text = self.filterObject.removeDuplicateLines()
        km = kmeans.Kmeans(matrix, text)
        return km.generateResponse()
