import sys
sys.path.append('..')
import unittest
import py_files.preprocessor as pre
from nltk.corpus import stopwords



class PreprocessorTest(unittest.TestCase):
    preprocessor = pre.Preprocessor('../tests/data/math/numpyMathFunctions.txt', 'how to compute cosine')

    def testInit(self):
        self.assertEqual(self.preprocessor.dataFolderPath, '../tests/data/math/numpyMathFunctions.txt')
        self.assertEqual(self.preprocessor.userInput, 'how to compute cosine')
        self.assertIsNotNone(self.preprocessor.lines)

    def testFetchData(self):
        self.assertIsNotNone(self.preprocessor.fetchData())

    def testGroupTextByParagraphs(self):
        self.assertIsNotNone(self.preprocessor.groupTextByParagraphs())
        self.assertEqual(len(self.preprocessor.groupTextByParagraphs().split('\n')), 1)
        self.assertNotEqual(self.preprocessor.groupTextByParagraphs().split('\n')[0], '')

    def testEnoughParagraphs(self):
        self.assertFalse(self.preprocessor.enoughParagraphs())

    def testGetParagraphs(self):
        self.assertIsNotNone(self.preprocessor.getParagraphs())

    def testRemoveEmptyLines(self):
        self.assertIsNotNone(self.preprocessor.removeEmptyLines())
        for line in self.preprocessor.removeEmptyLines():
            self.assertNotEqual(line, '')

    def testRemoveDuplicateLines(self):
        noDuplicateLines = self.preprocessor.removeDuplicateLines()
        self.assertIsNotNone(noDuplicateLines)
        for line in noDuplicateLines:
            noDuplicateLinesWithOutLine = noDuplicateLines
            del noDuplicateLinesWithOutLine[noDuplicateLines.index(line)]
            self.assertNotIn(line, noDuplicateLinesWithOutLine)

    def testAppendLoweredUserInput(self):
        self.assertIsNotNone(self.preprocessor.appendLoweredUserInput())
        self.assertEqual(self.preprocessor.appendLoweredUserInput()[-1], self.preprocessor.userInput)

    def testRemovePunctuation(self):
        self.assertNotIn(self.preprocessor.removePunctuations()[0], '.')

    def testRemoveStopWords(self):
        stops = set(stopwords.words('english'))
        for st in stops:
            self.assertNotIn(self.preprocessor.removeStopWords()[0], st)

    def testNegationHandling(self):
        negations = ["no", "not", "cant", "cannot", "never", "less", "without"]
        negations.append("barely")
        negations.append("hardly")
        negations.append("rarely")
        negations.append("noway")
        negations.append("didnt")
        for word in self.preprocessor.negationHandling():
            for neg in negations:
                self.assertNotEqual(neg, word)

    def testMeaningfulWords(self):
        self.assertIsNotNone(self.preprocessor.meaningfulWords())
        num = len(self.preprocessor.meaningfulWords())
        self.assertLessEqual(num, len(self.preprocessor.negationHandling()))

    def testStemming(self):
        self.assertIsNotNone(self.preprocessor.stemming())
        words = self.preprocessor.meaningfulWords()
        for w1, w2 in zip(self.preprocessor.stemming(), words):
            self.assertLessEqual(len(w1), len(w2))

    def testVectoriseData(self):
        data = self.preprocessor.vectoriseData()
        self.assertIsNotNone(data)
        self.assertEqual(data.shape[0], len(self.preprocessor.stemming()))

if __name__ == '__main__':
    unittest.main()
