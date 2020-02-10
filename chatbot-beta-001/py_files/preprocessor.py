import io
import os
import sys
import random
import string
import warnings
import numpy as np
import warnings
import nltk
from nltk.stem import WordNetLemmatizer
import re
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline, FeatureUnion


class Preprocessor:
    def __init__(self, dataFolderPath, userInput):
        self.dataFolderPath = dataFolderPath
        self.userInput = userInput

    def vectoriseData(self):
        vectorizer = Pipeline([('vectorizer', CountVectorizer()), ('tfidf', TfidfTransformer())])
        X = vectorizer.fit_transform(self.stemming())
        return X

    def stemming(self):
        words = str()
        stemmedWords = list()
        st=PorterStemmer()
        for line in self.meaningfulWords():
            words = ''
            for w in line.split():
                words += st.stem(w) + ' '
            stemmedWords.append(words.strip())
        return stemmedWords

    def meaningfulWords(self):
        meaningfulWords=[]
        words = str()
        tags=['VB','VBP','VBD','VBG','VBN','JJ','JJR','JJS','RB','RBR','RBS','UH',"NN",'NNP']
        text = self.negationHandling()
        for line in text:
            taggedWord = pos_tag(line.split())
            words = ''
            for w in taggedWord:
                if w[1] in tags:
                    words += w[0] + ' '
            meaningfulWords.append(words.strip())
        return meaningfulWords

    def negationHandling(self):
        counter=False
        modNegations=[]
        words = str()
        negations=["no","not","cant","cannot","never","less","without","barely","hardly","rarely","noway","didnt"]
        text = self.removeStopWords()
        for line in text:
            words = ''
            for i,j in enumerate(line.split()):
                if j in negations and i<len(line.split())-1:
                    words += str(line.split()[i]+'-'+line.split()[i+1]) + ' '
                    counter=True
                else:
                    if counter is False:
                        words += line.split()[i] + ' '
                    else:
                        counter=False
            modNegations.append(words.strip())
        return modNegations

    def removeStopWords(self):
        stop = set(stopwords.words('english'))
        stop.update(['compute', 'calculate', 'get', 'use'])
        words = str()
        noStops = list()
        for line in self.removePunctuations():
            words = ''
            for w in line.split():
                if w not in stop:
                    words += w + ' '
            noStops.append(words.strip())
        return noStops

    def removePunctuations(self):
        words = str()
        noPunctuations = list()
        text = self.fetchData().split('.')
        for line in text:
            words = ''
            for w in re.sub(r'[^\w\s]','',line).split():
                words += w + ' '
            noPunctuations.append(words.strip())
        return noPunctuations


    def fetchData(self):
        allFolders = os.listdir(self.dataFolderPath)
        rawData = str()
        for folder in allFolders:
            for data in os.listdir(self.dataFolderPath+'/'+folder):
                with open(self.dataFolderPath+folder+'/'+data,'r', encoding='utf8', errors ='ignore') as f:
                    rawData += f.read().lower()
        rawData += '\n' + self.userInput.lower()
        return rawData
