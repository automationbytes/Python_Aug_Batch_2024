import pytest

def test_greater():
    a = 10
    b = 5
    print("A is bigger number:" ,a,",",b ,"=", a>b)
    assert a>b == True

@pytest.mark.sanity
def test_lesser():
    a = 10
    b = 5
    print("A is smaller number:" ,a,",",b ,"=", a<b)
    assert a>b == True