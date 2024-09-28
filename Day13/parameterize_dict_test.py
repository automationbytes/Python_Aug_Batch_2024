import pytest


@pytest.mark.parametrize("input_values",[
    {"a":2,"b":3,"expectedsum":5},
    {"a":12,"b":13,"expectedsum":25},
    {"a":20,"b":30,"expectedsum":50},
    {"a":20,"b":3,"expectedsum":5},

])
def test_sumofnumbers(input_values):

    a = input_values["a"]
    b = input_values["b"]
    expectedsum = input_values["expectedsum"]

    assert a+b == expectedsum