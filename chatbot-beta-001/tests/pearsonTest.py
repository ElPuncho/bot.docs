import sys
sys.path.append('..')
import unittest
import numpy as np
from sklearn.cluster import KMeans
import py_files.pearson as p
import py_files.preprocessor as pre


class pearsonTest(unittest.TestCase):
    preprocessor = pre.Preprocessor('data/', 'how to compute base 10 logarithm')
    X = preprocessor.vectoriseData()
    sentences = preprocessor.fetchData().split('.')
    pearson = p.Pearson(X, sentences)

    def testInit(self):
        self.assertIsNotNone(self.pearson.tfidfMatrix)
        self.assertIsNotNone(self.pearson.pearsonCoeffs)
        self.assertIsNotNone(self.pearson.sentences)
        self.assertEqual(self.pearson.tfidfMatrix.shape[0], len(self.pearson.sentences))

    def testGetPearsonCoeffsOfUserInputAndData(self):
        self.assertIsNotNone(self.pearson.getPearsonCoeffsOfUserInputAndData())
        self.assertEqual(self.pearson.tfidfMatrix.shape[0], len(self.pearson.getPearsonCoeffsOfUserInputAndData()))

    def testGetIndexOfTopKMatches(self):
        topKMatches = 3
        self.assertIsNotNone(self.pearson.getIndexOfTopKMatches(topKMatches))
        self.assertEqual(len(self.pearson.getIndexOfTopKMatches(topKMatches)), topKMatches)

    def testGenerateResponse(self):
        self.assertIsNotNone(self.pearson.generateResponse())
        print(self.pearson.generateResponse())


if __name__ == '__main__':
    unittest.main()
