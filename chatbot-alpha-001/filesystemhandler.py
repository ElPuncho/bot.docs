#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

class FileSystemHandler:
    def __init__(self):
        self.createRootDirectory()
    
    def createRootDirectory(self):
        if not os.path.isdir(self.getRootDirectory()):
            os.mkdir(self.getRootDirectory())
            
    def getRootDirectory(self):
        return os.getcwd() + self.getSlashForOsVersion() + "data" 
            
    def getSlashForOsVersion(self):
        if os.name == "posix":
            return "/"
        return "\\"
    
    def getSearchFilePath(self, subdir, filename):
        return self.getRootDirectory() + self.getSlashForOsVersion() + subdir + self.getSlashForOsVersion() + filename
    
    def deleteSessionTempFiles(self, folder):
        for filename in os.listdir(folder):
            if os.path.isdir(folder + self.getSlashForOsVersion() + filename):
                self.deleteSessionTempFiles(folder + self.getSlashForOsVersion() + filename)
                os.rmdir(folder + self.getSlashForOsVersion() + filename)
            else:
                os.remove(folder + self.getSlashForOsVersion() + filename)
            
if __name__ == "__main__":
    h = FileSystemHandler()
    h.deleteSessionTempFiles(h.getRootDirectory())