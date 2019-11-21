import io
import os
import random
import string
import warnings
import numpy as np
from scipy.stats import pearsonr
from scipy import sparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
import nltk
from nltk.stem import WordNetLemmatizer


class CollaborativeFiltering:

    warnings.filterwarnings('ignore')
    nltk.download('popular', quiet=True)

    #uncomment the following only the first time
    #nltk.download('punkt') # first-time use only
    #nltk.download('wordnet') # first-time use only

    def __init__(self, dataFolderPath, user_input):
        self.dataFolderPath = dataFolderPath
        self.sentences_tokens = list()
        self.buildSentencesTokens()
        self.user_input = user_input


    def fetchData(self):
        all_folder = os.listdir(self.dataFolderPath)
        raw_data = str()
        for folder in all_folder:
            for data in os.listdir(self.dataFolderPath+'/'+folder):
                with open(self.dataFolderPath+folder+'/'+data,'r', encoding='utf8', errors ='ignore') as f:
                    raw_data += f.read().lower()
        return raw_data

    def buildSentencesTokens(self):
        table = {10 : ' '}
        self.sentences_tokens = list(set([token.strip().translate(table) for token in nltk.sent_tokenize(self.fetchData())]))

    def lemmatiseTokens(self, tokens):
        lemmer = WordNetLemmatizer()
        return [lemmer.lemmatize(token) for token in tokens]

    def normaliseLemmatisedTokens(self, data):
        remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
        return self.lemmatiseTokens(nltk.word_tokenize(data.lower().translate(remove_punct_dict)))

    def pearson_coeffs(self, x , Y):
        coeff = list()
        for i in range(Y.shape[0]):
            coeff.append((pearsonr(x.toarray()[0], Y.getrow(i).toarray()[0]))[0])
        return coeff

    def vectoriseData(self):
        self.sentences_tokens.append(self.user_input)
        TfidfVec = TfidfVectorizer(tokenizer=self.normaliseLemmatisedTokens, stop_words='english')
        tfidf = TfidfVec.fit_transform(self.sentences_tokens)
        return tfidf

    def getPearsonCoeffs(self):
        tfidf = self.vectoriseData()
        return np.asarray(self.pearson_coeffs(tfidf[-1], tfidf))

    def correlationMatch(self, pearson_coeffs):
        highestCorrelation = np.sort(pearson_coeffs)[-2]

        if(highestCorrelation<=0):
            return False
        else:
            return True

    def getIndexOfTopKMatches(self, sim_coeffs, k):
        index_top_k_sentences = sim_coeffs.argsort()[-(k+1):-1]
        return index_top_k_sentences

    def generateResponse(self):
        response = str()
        pearson_coeffs = self.getPearsonCoeffs()
        index_top_k_sentences = self.getIndexOfTopKMatches(pearson_coeffs, 3)

        if(self.correlationMatch(pearson_coeffs)):
            for i in range(index_top_k_sentences.size-1, 0, -1):
                response += self.sentences_tokens[index_top_k_sentences[i]]+"\n"
            return response
        else:
            response += "Sorry dont know about that one"
            return response

if __name__ == "__main__":
    filter = CollaborativeFiltering('data/', "array")
    print(filter.generateResponse())
