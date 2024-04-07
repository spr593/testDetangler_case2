import unittest

class featureB:
    def __init__(self, x = 0, y= 0):
        self.x = x
        self.y = y

    def action(self):
        return self.x + self.y

class testFeatureB(unittest.TestCase):
    def test_featureB(self):
        self.assertIsInstance(featureB.action(), (int,float), "Not numeric result")