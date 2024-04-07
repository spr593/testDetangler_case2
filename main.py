import unittest
from feature2 import *
from feature3 import *

if __name__=="__main__":
    objB = featureB(7,9)
    suite = unittest.TestLoader().loadTestsFromTestCase(testFeatureB)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if result.wasSuccessful():
        print("Tests-B passed")
    else:
        print("Tests-B failed")
    
    objC = featureC(2,3)
    suite = unittest.TestLoader().loadTestsFromTestCase(testFeatureC)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if result.wasSuccessful():
        print("Tests-C passed")
    else:
        print("Tests-C failed")

