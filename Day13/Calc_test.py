
def test_calc_add():
    a = 10
    b = 5
    print("Sum of the numbers:" ,a,"+",b ,"=", a+b)
    assert a+b == 15



def test_calc_sub():
    a = 10
    b = 5
    print("Difference of the numbers:" ,a,"-",b ,"=", a-b)
    assert a-b == 5

def test_mul_calc():
    a = 10
    b = 5
    print("Product of the numbers:" ,a,"*",b ,"=", a*b)
    assert a*b == 50

def test_div():
    a = 10
    b = 5
    print("Difference of the numbers:" ,a,"/",b ,"=", a/b)
    assert a//b == 5


def test_sum():
    a = 100
    b = 50
    print("Sum of the numbers:" ,a,"+",b ,"=", a+b)
    assert a+b == 15