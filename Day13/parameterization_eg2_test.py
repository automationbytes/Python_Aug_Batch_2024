import pytest


def inputvalues():
    return[
    (2,3,5),
    (10,5,15),
    (5,20,25),
    (-1,1,0),
    (10,4,15)
]


@pytest.mark.parametrize("a,b,expectedsum",inputvalues())
def test_sumofnumbers(a,b,expectedsum):
    assert a+b == expectedsum