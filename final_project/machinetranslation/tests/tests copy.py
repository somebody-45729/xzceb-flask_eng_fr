import unittest

from translator import english_to_french, french_to_english

class testFrench_to_English(unittest.TestCase):
    def test(self):
        self.assertEqual(french_to_english(""),"") # Test null input
        self.assertEqual(french_to_english("Hello"),"Bonjour") # Test translation

class testEnglish_to_French(unittest.TestCase):
    def test(self):
        self.assertEqual(english_to_french(""),"") # Test null input
        self.assertEqual(english_to_french("Bonjour"),"Hello") # Test translation