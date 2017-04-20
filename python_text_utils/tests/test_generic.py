# -*- coding: utf-8 -*-

import unittest

from python_text_utils.generic import Generic

class TestGeneric(unittest.TestCase):

    def test_strip_punctuation_unicode(self):
        with_punctuation = 'this-is.a!string@with#punctuation$symbols^only'
        without_punctuation = u'this is a string with punctuation symbols only'
        self.assertEqual(Generic.strip_punctuation_unicode(with_punctuation),
                         without_punctuation)

    def test_to_unicode(self):
        non_unicode = 'unicode'
        unicode = u'unicode'
        self.assertEqual(Generic.to_unicode(non_unicode),
                         unicode)