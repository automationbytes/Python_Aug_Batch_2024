import unittest

class UnitTestFixtures(unittest.TestCase):

    #Equals
    def test1(self):
        self.assertEqual(2+2,4)

    #not equals
    def test2(self):
        self.assertNotEqual(2 + 2, 4)

    def test3(self):
        self.assertTrue(2 + 2 == 4)



    def test4(self):
        self.assertFalse(2 + 2 == 4)

    #assert the object - assertis

    def test5(self):
        a = []
        b = a
        c = []
        self.assertIs(a,b)
        self.assertIs(a,c)



    def test6(self):
        a = []
        b = a
        c = []
        self.assertIsNot(a,c)

    def test7(self):
        a = [1,2,3,4,5]
        b = 3
        self.assertIn(b,a)

    #not in

    #isinstance
    def test9(self):
        a = "hello"
        b = int
        self.assertIsInstance(a,b)