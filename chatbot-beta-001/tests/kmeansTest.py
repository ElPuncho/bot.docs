import sys
sys.path.append('..')
import unittest
import numpy as np
from sklearn.cluster import KMeans
import py_files.kmeans as km
import py_files.preprocessor as pre

class kmeansTest(unittest.TestCase):
    preprocessor = pre.Preprocessor('data/', 'how to compute base 10 logarithm')
    X = preprocessor.vectoriseData()
    sentences = preprocessor.fetchData().split('.')
    kmeans = km.Kmeans(X, sentences)

    def testInit(self):
        self.assertIsNotNone(self.kmeans.tfidfMatrix)
        self.assertIsNotNone(self.kmeans.sentences)
        self.assertEqual(self.kmeans.tfidfMatrix.shape[0], len(self.kmeans.sentences))

    def testGenerateModel(self):
        self.assertIsNotNone(self.kmeans.generateModel())
        self.assertEqual(self.kmeans.tfidfMatrix.shape[0], len(self.kmeans.generateModel()))

    def testGetRelevantSentences(self):
        self.assertIsNotNone(self.kmeans.getRelevantSentences())


if __name__ == '__main__':
    unittest.main()
