# -*- coding: utf-8 -*-

import unittest

from ..greek import remove_accent

class TestRemoveAccent(unittest.TestCase):

    def test_remove_accent_from_greek_string_with_accent(self):
        with_accent = u'λόγος'
        without_accent = u'λογος'
        self.assertEqual(remove_accent(with_accent), without_accent)

    def test_remove_accent_from_greek_string_without_accent(self):
        without_accent = u'πιτα'
        self.assertEqual(remove_accent(without_accent), without_accent)

    def test_remove_accent_from_latin_string(self):
        latin_string = u'whatever'
        self.assertEqual(remove_accent(latin_string), latin_string)

    def test_remove_accent_non_unicode(self):
        with_accent = 'λόγος'
        without_accent = u'λογος'
        self.assertEqual(remove_accent(with_accent), without_accent)