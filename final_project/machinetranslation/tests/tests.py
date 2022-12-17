import unittest
from translator import englishToFrench, frenchToEnglish

class testFrenchToEnglish(unittest.TestCase):
    def testF2E(self):
        self.assertEqual(frenchToEnglish(None), None)
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

class testEngishToFrench(unittest.TestCase):
     def testE2F(self):
        self.assertEqual(englishToFrench(None), None)
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

if __name__ == '__main__':
    unittest.main()