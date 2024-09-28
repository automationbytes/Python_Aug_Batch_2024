import pytest

@pytest.mark.dependancy()
def test_login():
    assert True, "Login Issue"

@pytest.mark.dependency(depends = ["test_login"])
def test_homePage():
    assert True

@pytest.mark.dependency(depends = ["test_login"])
def test_Logout():
    assert True

