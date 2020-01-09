import sys
sys.path.append('..')
import unittest
from scipy.stats import pearsonr
import nltk
import py_files.preprocessor as pre
import numpy as np
from nltk.corpus import stopwords
from nltk.tag import pos_tag


class PreprocessorTest(unittest.TestCase):
    preprocessor = pre.Preprocessor('data/', 'how to compute cosine')

    def testInit(self):
        self.assertEqual(self.preprocessor.dataFolderPath, 'data/')
        self.assertEqual(self.preprocessor.userInput, 'how to compute cosine')

    def testFetchData(self):
        self.assertIsNotNone(self.preprocessor.fetchData())

    def testRemovePunctuation(self):
        self.assertNotIn(self.preprocessor.removePunctuations()[0], '.')

    def testRemoveStopWords(self):
        stops = set(stopwords.words('english'))
        for st in stops:
            self.assertNotIn(self.preprocessor.removeStopWords()[0], st)

    def testNegationHandling(self):
        negations=["no","not","cant","cannot","never","less","without","barely","hardly","rarely","noway","didnt"]
        for word in self.preprocessor.negationHandling():
            for neg in negations:
                self.assertNotEqual(neg, word)

    def testMeaningfulWords(self):
        self.assertIsNotNone(self.preprocessor.meaningfulWords())
        self.assertLessEqual(len(self.preprocessor.meaningfulWords()), len(self.preprocessor.negationHandling()))

    def testStemming(self):
        self.assertIsNotNone(self.preprocessor.stemming())
        for w1, w2 in zip(self.preprocessor.stemming(), self.preprocessor.meaningfulWords()):
            self.assertLessEqual(len(w1), len(w2))

    def testVectoriseData(self):
        self.assertIsNotNone(self.preprocessor.vectoriseData())
        self.assertEqual(self.preprocessor.vectoriseData().shape[0], len(self.preprocessor.stemming()))

if __name__ == '__main__':
    unittest.main()
