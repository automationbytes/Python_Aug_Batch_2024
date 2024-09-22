import unittest

class UnitTestFixtures(unittest.TestCase):

    @unittest.skip("Skipping the test1")
    def test1(self):
        print("test1")

    @unittest.skipIf(1 == 0,"Skip if my condition is true")
    def test2(self):
        print("test2")

    @unittest.skipUnless(1 == 0, "Skip if my condition is false")
    def test3(self):
        print("test3")

    def test4(self):
        print("Hello Test")
        self.skipTest("Skipping after this statment")
        print("test4")

    @unittest.expectedFailure
    def test5(self):
        self.assertTrue(False)
