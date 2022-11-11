from twttr import del_vowels


def test_no_vowel():
    assert del_vowels("wrd") == "wrd"


def test_capital_vowel():
    assert del_vowels("Assert") == "ssrt"


def test_lower_vowel():
    assert del_vowels("assert") == "ssrt"


def test_numbers():
    assert del_vowels("CS50") == "CS50"


def test_upper_vowel():
    assert del_vowels("ASSERT") == "SSRT"


def test_punctuation():
    assert del_vowels("CS50!") == "CS50!"