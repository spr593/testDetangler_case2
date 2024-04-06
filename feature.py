import unittest

class featureA:
    def __init__(self, x = 0, y= 0):
        self.x = x
        self.y = y

    def action(self):
        return self.x*self.y

class testFeatureA(unittest.TestCase):
    def test_featureA(self):
        self.assertIsInstance(featureA.action(), (int,float), "Not numeric result")
        

if __name__ == "__main__":
    obj = featureA(3,5)
    unittest.main()