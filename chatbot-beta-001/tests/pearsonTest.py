import sys
sys.path.append('..')
import unittest
import py_files.pearson as p
import py_files.preprocessor as pre



class pearsonTest(unittest.TestCase):
    query = 'how to compute base 10 logarithm'
    preprocessor = pre.Preprocessor('../tests/data/math/numpyMathFunctions.txt', query)
    X = preprocessor.vectoriseData()
    sentences = preprocessor.removeDuplicateLines()
    pearson = p.Pearson(X, sentences)

    def testInit(self):
        self.assertIsNotNone(self.pearson.tfidfMatrix)
        self.assertIsNotNone(self.pearson.pearsonCoeffs)
        self.assertIsNotNone(self.pearson.sentences)
        lenPearson = len(self.pearson.sentences)
        self.assertEqual(self.pearson.tfidfMatrix[:-1].shape[0], lenPearson)

    def testGetPearsonCoeffsOfUserInputAndData(self):
        self.assertIsNotNone(self.pearson.getPearsonCoeffsOfUserInputAndData())
        lenPearson = len(self.pearson.getPearsonCoeffsOfUserInputAndData())
        self.assertEqual(self.pearson.tfidfMatrix[:-1].shape[0], lenPearson)

    def testGetIndexOfTopKMatches(self):
        topKMatches = 3
        index = self.pearson.getIndexOfTopKMatches(topKMatches)
        self.assertIsNotNone(index)
        self.assertEqual(len(index), topKMatches)

    def testGenerateResponse(self):
        self.assertIsNotNone(self.pearson.generateResponse())


if __name__ == '__main__':
    unittest.main()
