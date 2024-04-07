import unittest

class featureC:
    def __init__(self, x = 0, y= 0):
        self.x = x
        self.y = y

    def action(self):
        return self.x - self.y

class testFeatureC(unittest.TestCase):
    def test_featureC(self):
        self.assertIsInstance(featureC.action(), (int,float), "Not numeric result")