from seasons import get_date

def test_format():
    assert get_date("2021-10-28") == "Five hundred twenty-five thousand, six hundred minutes"

