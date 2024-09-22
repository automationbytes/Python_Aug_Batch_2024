import unittest

class UnitTestFixtures(unittest.TestCase):

    #setup- before
    #teardown - after

    def setUp(self):
        print("Setup Test")

    def test3(self):
        print("Hello Test 3")


    def test2(self):
        print("Hello Test 2")

    def tearDown(self):
        print("TearDown Test")

if __name__ == '__main__':
    unittest.main()