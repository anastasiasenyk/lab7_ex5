"""Vinegere decode encode"""


class VigenereCipher:
    """Vinegere"""
    def __init__(self, keyword):
        """
        :param keyword:
        >>> vin = VigenereCipher("TRAIN")
        >>> vin.keyword
        'TRAIN'
        """
        self.keyword = keyword

    def _code(self, text, combine_func):
        """
        :param text: str
        :param combine_func: str
        :return: str
        >>> vin = VigenereCipher("TRAIN")
        >>> vin._code('E', combine_character)
        'X'
        """
        text = text.replace(" ", "").upper()
        combined = []
        keyword = self.extend_keyword(len(text))
        for p, k in zip(text, keyword):
            combined.append(combine_func(p, k))
        return "".join(combined)

    def encode(self, plaintext):
        """
        :param plaintext: str
        :return: str
        >>> vin = VigenereCipher("TRAIN")
        >>> vin.encode('E')
        'X'
        """
        return self._code(plaintext, combine_character)

    def decode(self, ciphertext):
        """
        :param ciphertext: str
        :return: str
        >>> vin = VigenereCipher("TRAIN")
        >>> vin.decode("XECWQXUIVCRKHWA")
        'ENCODEDINPYTHON'
        """
        return self._code(ciphertext, separate_character)

    def extend_keyword(self, number):
        """
        :param number: int
        :return: str
        >>> vin = VigenereCipher("TRAIN")
        >>> vin.extend_keyword(16)
        'TRAINTRAINTRAINT'
        """
        repeats = number // len(self.keyword) + 1
        return (self.keyword * repeats)[:number]


def combine_character(plain, keyword):
    """
    :param plain: str
    :param keyword: str
    :return: str
    >>> combine_character('E', 'T')
    'X'
    """
    plain = plain.upper()
    keyword = keyword.upper()
    plain_num = ord(plain) - ord('A')
    keyword_num = ord(keyword) - ord('A')
    return chr(ord('A') + (plain_num + keyword_num) % 26)


def separate_character(cypher, keyword):
    """
    :param cypher: str
    :param keyword: str
    :return: str
    >>> separate_character('E', 'T')
    'L'
    """
    cypher = cypher.upper()
    keyword = keyword.upper()
    cypher_num = ord(cypher) - ord('A')
    keyword_num = ord(keyword) - ord('A')
    return chr(ord('A') + (cypher_num - keyword_num) % 26)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
