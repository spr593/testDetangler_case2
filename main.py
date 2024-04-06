from feature import featureA
from feature import testFeatureA
from feature2 import featureB
from feature2 import testFeatureB
import unittest

if __name__=="__main__":
    objA = featureA(7,9)
    suiteA = unittest.TestLoader().loadTestsFromTestCase(testFeatureA)
    runner = unittest.TextTestRunner()
    result = runner.run(suiteA)
    if result.wasSuccessful():
        print("TestsA passed")
    else:
        print("TestsA failed")

    objB = featureB (6,3)
    suiteB = unittest.TestLoader().loadTestsFromTestCase(testFeatureB)
    runner = unittest.TextTestRunner()
    result = runner.run(suiteB)
    if result.wasSuccessful():
        print("TestsB passed")
    else:
        print("TestsB failed")


