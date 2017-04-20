from unicodedata import normalize

from python_text_utils.generic import Generic


class Greek(object):
    """
    Class containing text utils for the greek language.
    """

    @classmethod
    def strip_accent_unicode(cls, text):
        """
        Removes accents from greek unicode or str string.
        Only greek accent (u'\u0301') is removed.

        :param text:        unicode or str string.
        :return:            returns unicode string without accents.
        """
        accent = u'\u0301'
        text = Generic.to_unicode(text)
        return normalize('NFC', ''.join(
            ch
            for ch in normalize('NFD', text)
            if ch not in [accent]
        ))

    @classmethod
    def strip_punctuation_and_accent_unicode(cls, text):
        """
        Converts string to unicode (if str), removes punctuation and accent.
        Only greek accent (u'\u0301') is removed.

        :param text:        unicode or str string.
        :return:            unicode string lowercase, without accents and punctuation.
        """
        text = Generic.to_unicode(text)
        return Generic.strip_punctuation_unicode(cls.strip_accent_unicode(text))


