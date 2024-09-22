import unittest

def setUpModule():
    print("Setup Module Level")


def tearDownModule():
    print("Tear Down Module Level")


class UnitTestFixtures(unittest.TestCase):

    #setup- before
    #teardown - after

    @classmethod
    def setUpClass(cls):
        print("SetUp class")


    @classmethod
    def tearDownClass(cls):
        print("TearDown class")
    def setUp(self):
        print("Setup Test")

    def test3(self):
        print("Hello Test 3")


    def test2(self):
        print("Hello Test 2")

    def tearDown(self):
        print("TearDown Test")
class UnitTestFixtures1(unittest.TestCase):

    #setup- before
    #teardown - after

    @classmethod
    def setUpClass(cls):
        print("SetUp class1")


    @classmethod
    def tearDownClass(cls):
        print("TearDown class1")
    def setUp(self):
        print("Setup Test1")

    def test13(self):
        print("Hello Test 13")


    def test12(self):
        print("Hello Test 12")

    def tearDown(self):
        print("TearDown Test1")

if __name__ == '__main__':
    unittest.main()