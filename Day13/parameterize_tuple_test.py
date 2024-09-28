import pytest


@pytest.mark.parametrize("input_values,expectedsum",[
    ((2,3),5),
    ((10,5),15),
    ((5,20),25),
    ((-1,1),0),
    ((10,4),15)
])
def test_sumofnumbers(input_values,expectedsum):
    a,b = input_values
    assert a+b == expectedsum