#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import py_files.controller as con

def newLineRemover(string):
    return string.replace("\n", "")

def getSlashForOsVersion():
        if os.name == "posix":
            return "/"
        return "\\"

def saveCSVFile(filePath, results, headers):
    file = open(filePath, "a+")
    file.write(headers + "\n")
    for key in results.keys():
        file.write(newLineRemover(key) + ";" + newLineRemover(results[key]) + "\n")
    file.close()
    
def loadCSVFile(filePath):
    data, file = dict(), open(filePath).readlines()
    for i in range(1, len(file)):
        data[file[i].split(";")[0]] = file[i].split(";")[1]
    return data
    
def compareCSVFfiles(csvA, csvB):
    compareResults = dict()
    assert len(csvA) == len(csvB)
    for key in csvA.keys():
        if newLineRemover(csvA[key]) == newLineRemover(csvB[key]):
            compareResults[key] = "True"
        else:
            compareResults[key] = "False"
    return compareResults

if __name__ == "__main__":
    results, testDir = dict(), os.getcwd() + getSlashForOsVersion() + "testDataForAccuracy" + getSlashForOsVersion()
    
    testData = open(testDir + "testQueries.txt").readlines()
    for query in testData:
        c = con.ControlManager(query)
        c.initSession()
        c.crawlQuery()
        results[query] = c.executeFiltering()
        
    saveCSVFile(testDir + "testResults.csv", results, "Query;Result")
    perfectResults = loadCSVFile(testDir + "testResults.csv")
    saveCSVFile(testDir + "compareResults.csv", compareCSVFfiles(perfectResults, perfectResults), "Query;testResults == intendedResult")
    
    