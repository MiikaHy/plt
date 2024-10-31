import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_get_phrase(self):
        translator = PigLatin("hello world")
        self.assertEqual("hello world", translator.get_phrase())

    def test_get_nil_phrase(self):
        translator = PigLatin("")
        self.assertEqual("nil", translator.translate())

    def test_word_ends_with_y(self):
        translator = PigLatin("hey")
        self.assertEqual("heynay", translator.translate())
