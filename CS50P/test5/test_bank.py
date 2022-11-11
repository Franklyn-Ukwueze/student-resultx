import bank



def test_incorrect():
    assert bank.value("Greetings") == "$100"


def test_case_insensitivity():
    assert bank.value("HELLO") == "$0"
    assert bank.value("hello") == "$0"


def test_entire_phrase():
    assert bank.value("Hello, world") == "$0"
    assert bank.value("Greetings, world") == "$100"
    assert bank.value("Hi, world") == "$20"