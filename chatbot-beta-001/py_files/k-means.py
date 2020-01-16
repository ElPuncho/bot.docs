import numpy as np
from sklearn.cluster import KMeans
import sys
import preprocessor

class Kmeans:
    def __init__(self, tfidfMatrix, sentences):
        self.tfidfMatrix = tfidfMatrix
        self.sentences = sentences

    def generateModel(self):
        kmeans = KMeans(n_clusters=int(len(self.sentences)/3))
        kmeans.fit_predict(X)
        labels = kmeans.predict(X)
        kmeans.cluster_centers_
        return labels

    def getRelevantSentences(self):
        relevantSentences = str()
        labels = self.generateModel()
        idx = np.where(labels == labels[-1])
        for i in idx[0][:-1]:
            relevantSentences += self.sentences[int(i)] + '\n'
        return relevantSentences
