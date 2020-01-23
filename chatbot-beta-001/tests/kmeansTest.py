import sys
import unittest
import py_files.kmeans as km
import py_files.preprocessor as pre
sys.path.append('..')


class kmeansTest(unittest.TestCase):
    query = 'how to compute base 10 logarithm'
    preprocessor = pre.Preprocessor('data/', query)
    X = preprocessor.vectoriseData()
    sentences = preprocessor.fetchData().split('.')
    kmeans = km.Kmeans(X, sentences)

    def testInit(self):
        self.assertIsNotNone(self.kmeans.tfidfMatrix)
        self.assertIsNotNone(self.kmeans.sentences)
        lenKMeans = len(self.kmeans.sentences)
        self.assertEqual(self.kmeans.tfidfMatrix.shape[0], lenKMeans)

    def testGenerateModel(self):
        self.assertIsNotNone(self.kmeans.generateModel())
        lenKMeans = len(self.kmeans.generateModel())
        self.assertEqual(self.kmeans.tfidfMatrix.shape[0], lenKMeans)

    def testGetRelevantSentences(self):
        self.assertIsNotNone(self.kmeans.getRelevantSentences())


if __name__ == '__main__':
    unittest.main()
