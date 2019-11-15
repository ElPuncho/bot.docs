#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests
from bs4 import BeautifulSoup 

class Crawler:
    
    def __init__(self, query):
        self.query = query
        self.rootDirectory = os.getcwd() + self.getSlashForOsVersion() + "data" + self.getSlashForOsVersion()
    
    def getSlashForOsVersion(self):
        if os.name == "posix":
            return "/"
        return "\\"
        
    def checkDirElseMkDir(self, folder):
        if not os.path.isdir(folder):
            os.mkdir(folder)
        
    def getLibUrl(self):
        searchUrl = "https://api.duckduckgo.com/?q=" + self.query.split(":")[0] + " " + self.query.split(":")[1] + "&format=json&pretty=1"
        request = requests.get(searchUrl)
        data = request.json()
        return data["AbstractURL"]
    
    def getTextFromWebsite(self, URL):
        request = requests.get(URL)
        soup = BeautifulSoup(request.content,'html.parser')
        for s in soup(['script', 'style']):
            s.decompose()
        return soup
    
    def writeTextToFile(self, soup):
        self.checkDirElseMkDir(self.rootDirectory + self.query.split(":")[0])
        file = open(self.rootDirectory + self.query.split(":")[0] + self.getSlashForOsVersion() + self.query.split(":")[1] + ".txt", "w", encoding = "utf8")
        for div_tag  in soup(["p", "div"]):
            file.write(div_tag.text)
        file.close()

if __name__ == "__main__":
    c = Crawler("python:min:how to array")
    c.writeTextToFile(c.getTextFromWebsite(c.getLibUrl()))
    