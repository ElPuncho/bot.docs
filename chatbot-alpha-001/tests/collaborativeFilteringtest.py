import sys
sys.path.append('..')
import unittest
from scipy.stats import pearsonr
import nltk
import py_files.collaborativeFiltering as cf
import numpy as np


class collaborativeFilteringtest(unittest.TestCase):

    filter = cf.CollaborativeFiltering('data/', 'python:math: how to use cosine')

    def testInit(self):
        self.assertEqual(self.filter.dataFolderPath, 'data/')
        self.assertEqual(self.filter.user_input, 'python:math: how to use cosine')
        self.assertIsNotNone(self.filter.sentences_tokens)

    def testFetchData(self):
        self.assertIsNotNone(self.filter.fetchData())
        self.assertIn(self.filter.sentences_tokens[0], self.filter.fetchData())

    def testBuildSentencesTokens(self):
        self.assertIsNotNone(self.filter.buildSentencesTokens())
        self.assertIsInstance(self.filter.buildSentencesTokens(), list)

    def testLemmatiseTokens(self):
        self.assertIsNotNone(self.filter.lemmatiseTokens(self.filter.sentences_tokens))

    def testNormaliseLemmatisedTokens(self):
        self.assertIsNotNone(self.filter.normaliseLemmatisedTokens(self.filter.fetchData()))
        self.assertNotIn(self.filter.normaliseLemmatisedTokens(self.filter.fetchData())[0], '.')
        self.assertEqual(self.filter.normaliseLemmatisedTokens(self.filter.fetchData())[0],
                        self.filter.normaliseLemmatisedTokens(self.filter.fetchData())[0].lower())

    def testVectoriseData(self):
        self.assertIsNotNone(self.filter.vectoriseData())
        self.assertEqual(self.filter.vectoriseData().shape[0], len(self.filter.sentences_tokens)+1)

    def testPearsonCoeffs(self):
        p = self.filter.vectoriseData()[-1]
        self.assertEqual(self.filter.pearson_coeffs(p, p)[0], 1.0)

    def testGetPearsonSimOfUserInputAndData(self):
        self.assertEqual(len(self.filter.sentences_tokens)+1, len(self.filter.getPearsonSimOfUserInputAndData()))

    def testCorrelationMatch(self):
        self.assertFalse(self.filter.correlationMatch(np.array([0,1])))
        self.assertTrue(self.filter.correlationMatch(np.array([1,2])))

    def testGetIndexOfTopKMatches(self):
        self.assertIsNotNone(self.filter.getIndexOfTopKMatches(self.filter.getPearsonSimOfUserInputAndData(), 1))
        self.assertEqual(len(self.filter.getIndexOfTopKMatches(self.filter.getPearsonSimOfUserInputAndData(), 1)), 1)
        self.assertIsInstance(self.filter.getIndexOfTopKMatches(self.filter.getPearsonSimOfUserInputAndData(), 1), np.ndarray)

    def testGenerateResponse(self):
        self.assertEqual(self.filter.generateResponse()[0:3], 'cos')
        self.assertIsNotNone(self.filter.generateResponse())


if __name__ == '__main__':
    unittest.main()
