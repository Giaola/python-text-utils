from unicodedata import normalize

def remove_accent(text):
    """
    Removes accents from greek unicode or str string.

    :param text:    unicode or str string
    :return:        returns unicode string without accents
    """
    accent = u'\u0301'
    if isinstance(text, str):
        text = text.decode('utf-8')
    return normalize('NFC', ''.join(
        ch
        for ch in normalize('NFD', text)
        if ch not in [accent]
    ))
