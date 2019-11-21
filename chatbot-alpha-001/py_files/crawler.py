#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import py_files.filesystemhandler as fsh
from bs4 import BeautifulSoup 

class Crawler:
    
    def __init__(self, query):
        self.query = query
        self.handler = fsh.FileSystemHandler()
        self.rootDirectory = self.handler.getRootDirectory()
        
    def getLibUrl(self):
        #duckduckgo api url "https://api.duckduckgo.com/?q=" + self.query.split(":")[0] + " " + self.query.split(":")[1] + "&format=json&pretty=1"
        #duckduckgo json access data["AbstractURL"]
        searchUrl = "https://www.googleapis.com/customsearch/v1?q=" + self.query.split(":")[0] + " " + self.query.split(":")[1] + "&cx=007916430864706508896:5x4nlnwradj&key=AIzaSyBa0tj2m9x3k7ZbkKcia30TLiG6yzulFoY"
        request = requests.get(searchUrl)
        data = request.json()
        return data["items"][0]["formattedUrl"]
    
    def getTextFromWebsite(self, URL):
        request = requests.get(URL)
        soup = BeautifulSoup(request.content,'html.parser')
        for s in soup(['script', 'style']):
            s.decompose()
        return soup
    
    def writeTextToFile(self, soup):
        self.handler.checkDirElseMkDir(self.rootDirectory + self.handler.getSlashForOsVersion() + self.query.split(":")[0])
        file = open(self.rootDirectory + self.handler.getSlashForOsVersion() +  self.query.split(":")[0] + self.handler.getSlashForOsVersion() + self.query.split(":")[1] + ".txt", "w", encoding = "utf8")
        for div_tag  in soup(["p", "div"]):
            file.write(div_tag.text)
        file.close()
