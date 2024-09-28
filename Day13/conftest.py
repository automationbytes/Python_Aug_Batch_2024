import pytest


@pytest.mark.helper
def pytest_configure(config):
    config.addinivalue_line("markers", "sanity")


@pytest.fixture()
def input_a():
    return 10


@pytest.fixture()
def input_b():
    return 5
